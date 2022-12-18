# 7th day of Advent of Code 2022
# Matteo Martinelli

from pathlib import Path

class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    def __str__(self):
        return f'{self.name} (file, size={self.size})'

class Directory():
    def __init__(self, path: list = ['/'] ):
        self.path = path
        self.files = []
        self.directories = []
        self.files_size = 0
        self.name = path[-1]

    def add_file(self, file: File):
        self.files.append(file)
        self.files_size += file.size

    def add_dir(self, dir):
        self.directories.append(dir)

    def get_size(self):
        return self.files_size + sum([d.get_size() for d in self.directories])

    def __str__(self) -> str:
        #TODO can be optimized, with the number of tab corrected by relative_path
        tree  = f'- {self.name} (dir)\n'
        n_tab = len(self.path)
        for d in self.directories:
            tree += '\t'*n_tab + f'{d}'
        for f in self.files:
            tree+= '\t'*(n_tab) + f'- {f}\n'
        return tree
        
class FileSytem():
    def __init__(self):
        self.root = '/'
        self.directories = {'/' : Directory()}

    def add_dir(self, parent_dir: list, dir_name: str):
        parent_dir_str = '/'.join(parent_dir)[1:] if parent_dir != ['/'] else '/'
        path_str =  parent_dir_str + f'/{dir_name}' if parent_dir != ['/'] else f'/{dir_name}'
        dir_to_add = Directory(parent_dir+ [dir_name])
        self.directories[path_str] = dir_to_add
        self.directories[parent_dir_str].add_dir(dir_to_add)

    def add_file(self, parent_dir: list, file: File):
        parent_dir_str = '/'.join(parent_dir)[1:] if parent_dir != ['/'] else '/'
        self.directories[parent_dir_str].add_file(file)

    def __getitem__(self, keys):    
        path = '/'.join(keys)[1:] if keys != ['/'] else '/'
        return self.directories[path]

    def __str__(self, path: str = '/'):
        return f'{self.directories[path]}'


class Parser():
    
    def __init__(self, commands: list= []):
        self.path = ['/']
        self.commands = commands
        self.commands.append('EOF_TOKEN')
        self.root = FileSytem()
    
    def cd (self, cmd: str):
        key, _, tobe_dir = cmd.split(' ')
        #print(tobe_dir)
        if tobe_dir == '..':
            self.path.pop()
        elif tobe_dir == '/':
            self.path = ['/']
        else:
            self.path.append(tobe_dir)
            try:
                self.root[self.path]
            except:
                FileNotFoundError

    def ls (self, i_cmd: int):
        token, name = self.commands[i_cmd].split(' ')
        while  token != '$' and token != 'EOF_TOKEN':
            #print(token)
            if token == 'dir':
                name = self.commands[i_cmd].split(' ')[1]
                self.root.add_dir(self.path, name)
            else:
                name = self.commands[i_cmd].split(' ')[1]
                file = File(name=name, size=int(token))
                self.root.add_file(self.path, file)
            i_cmd+=1
            token = self.commands[i_cmd].split(' ')[0]
        return i_cmd
        
    def parse_dir(name :str):
        return name

    def parse_command(self, cmd: str, i_cmd: str):
        tokens = cmd.split()
        key = tokens[0]
        cmd_type = tokens[1]
        if key == '$':
            if cmd_type == 'cd':
                self.cd(cmd)
                return  i_cmd+1
            else:
                return self.ls(i_cmd+1)
        else:
            raise SyntaxError

    def build_file_system(self):
        i_cmd = 0
        token = self.commands[i_cmd].split(' ')[0]
        while token != 'EOF_TOKEN':
            #print(commands[i_cmd])
            i_cmd = self.parse_command(self.commands[i_cmd], i_cmd)
            token = self.commands[i_cmd].split(' ')[0]
        

file_in = Path('input') / 'day7.txt'

# pre-process
commands = file_in.open().read().splitlines()
        
parser = Parser(commands)
parser.build_file_system()
root = parser.root

# Part 1
small_directories = dict()
for path, d in root.directories.items():
    size = d.get_size()
    if size <= 100000:
        small_directories[path] = size

print(sum(small_directories.values()))

# Part 2
total_disk_space = 70000000
total_needed_space = 30000000
used_space = root.directories['/'].get_size()
space_to_free = total_needed_space - (total_disk_space - used_space)

big_directories = dict()
for path, d in root.directories.items():
    size = d.get_size()
    if size >= space_to_free:
        big_directories[path] = size

print(sorted(big_directories.values())[0])
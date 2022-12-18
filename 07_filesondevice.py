import os
import re
from collections import deque


dir_re = re.compile("dir (.+)")
file_re = re.compile("(\d+) (.+)")
cd_re = re.compile("cd (.+)")

class File:
    def __init__(self, name, parent, size):
        self.name = name 
        self.parent = parent
        self.size = size

    def __repr__(self):
        return f"file: {self.name} with size: {self.size}"


class Directory:
    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.children = children
        self.path_to_here = self.name if self.parent is None else self.parent.path_to_here + self.name + "/"

    def __repr__(self):
        return f"(dir: {self.name} with parent: {self.parent} and children {self.children})"


class Dfs:
    def __init__(self, name, pos, sizes):
        self.name = name 
        self.pos = pos 
        self.sizes = sizes

    def traverse(self):
        dir_children = [x for x in self.pos.children if isinstance(x, Directory)]
        filesizes = sum([fi.size for fi in self.pos.children if isinstance(fi, File)])
        if not dir_children:
            self.sizes[self.pos.path_to_here] = filesizes
            return filesizes

        cur_size = filesizes
        for child in self.pos.children:
            if isinstance(child, Directory):
                new_dfs = Dfs(child.name, child, self.sizes)
                cur_size += new_dfs.traverse()

        self.sizes[self.pos.path_to_here] = cur_size
        return cur_size


    def __repr__(self):
        return f"dfs from {self.name} with sizes {self.sizes}"




class Traverser:
    def __init__(self, pos, commands):
        self.pos = pos 
        self.commands = commands

    def __repr__(self):
        return f"""
            pointer to pos: {self.pos}
            commands remaining: {self.commands}
        """

    def traverse(self):
        while True:
            if len(self.commands) == 0:
                print(f"no more commands")
                break
            next_command = self.commands.popleft()
            print(f"------------next command is {next_command}")
            if next_command[0] == "ls":
                print(f"listing files")
                for i in range(1, len(next_command)):
                    print(next_command[i])
                    if dir_re.match(next_command[i]):
                        dirname = dir_re.match(next_command[i]).group(1)
                        print(f"directory matches: {dirname}")

                        # have we seen this directory before
                        seen = False
                        for child in self.pos.children:
                            if isinstance(child, Directory) and child.name == dirname:
                                print('we have seen dir before')
                                seen = True
                                continue
                        if not seen:
                            newdir = Directory(dirname, self.pos, [])
                            self.pos.children.append(newdir)

                    elif file_re.match(next_command[i]):
                        filesize = file_re.match(next_command[i]).group(1)
                        filename = file_re.match(next_command[i]).group(2)
                        newfile = File(filename, self.pos, int(filesize))
                        print(newfile)
                        self.pos.children.append(newfile)
                    else:
                        raise ValueError("command not handled")
            elif cd_re.match(next_command[0]):
                print(f"command is a change directory")
                path_to_take = cd_re.match(next_command[0]).group(1)
                print(f"path to take is {path_to_take}")
                if path_to_take == "..":
                    print("moving up one dir")
                    self.pos = self.pos.parent
                else:
                    found_dir = False
                    for child in self.pos.children:
                        if isinstance(child, Directory) and child.name == path_to_take:
                            print(f"found directory, navigating there")
                            found_dir = True
                            self.pos = child
                    if not found_dir:
                        raise ValueError("tried to navigate to unknown dir")

        print(f"finished traversing")




def process(data):
    dlist = data.split("\n$")
    dlist = [x.strip() for x in dlist]
    dlist = [ x.split("\n") for x in dlist]
    dq = deque(dlist)
    print(dq)
    
    c = dq.popleft()
    print(c)
    root = Directory("/", None, [])
    me = Traverser(root, dq)
    
    print(me)
    me.traverse()

    dfs = Dfs("/", root, {})
    dfs.traverse()
    print(dfs.sizes)

    dirs_less_than_100k = [x for x in dfs.sizes.values() if x <= 100000]
    print(dirs_less_than_100k)

    print(f"the answer is {sum(dirs_less_than_100k)}")






def run_part_1(sample_or_real):
    if sample_or_real == "sample":
        whichfile = "sample07.txt"
    elif sample_or_real == "real":
        whichfile = "problem07.txt"
    else:
        raise ValueError("invalid func call param - must be real or sample")

    file = os.path.join("input_files", whichfile)

    with open(file, "r") as f:
        data = f.read()

    print(data)
    process(data)




def run_part_2():
    pass

if __name__ == "__main__":
    while True:
        which_one_to_run = input("which part to run? enter 1 or 2:\n")
        if which_one_to_run in ("1", "2"):
            print("good choice")
            break

    if which_one_to_run == "1":
        run_part_1("sample")
        run_part_1("real")
    else:
        run_part_2()
#!/usr/bin/env python3

from collections import defaultdict

# for each line, keep stack of the current path
# for "$ cd ..", pop the current directory off from the stack
# for "$ cd [dir_name]", append dir to the stack
# for "$ ls", do nothing (assume that we only call ls once in directory to show contents)
# for "dir", do nothing
# for "[file_size] file_name", add file_size to all directories in current path stack

cmds = []

def storeDirSizes(cmds: list[str]) -> dict[int, int]:
    dirSizes = defaultdict(int)
    pathStack = []
    dirID = 0

    for cmd in cmds:
        if cmd[0] == '$':
            cmdItems = cmd.split()
            cmdName = cmdItems[1]

            match cmdName:
                case "cd":
                    cmdVar = cmdItems[2]
                    if cmdVar == "..":
                        pathStack.pop()
                    else:
                        # as dir name (cmdVar) is not unique, we will replace the dir name with a unique increasing id
                        pathStack.append(dirID)
                        dirID += 1
        else:
            # treat it as the output of the ls cmd
            fileType, _ = cmd.split()

            if fileType.isdigit():
                fileSize = int(fileType)

                for dir in pathStack:
                    dirSizes[dir] += fileSize
    
    return dirSizes

# get sum of all directories with size <= 100000
def sumDirSizes(dirSizes: dict[int, int]) -> int:
    return sum([x for x in dirSizes.values() if x <= 100000])

with open('7/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            cmds.append(strippedLine)

    f.close()

dirSizes = storeDirSizes(cmds)
print(sumDirSizes(dirSizes))
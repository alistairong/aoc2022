#!/usr/bin/env python3

from collections import defaultdict
import re

# crates = {
#     # 1: ["W","M","L","F"],
#     # 2: ["B","Z","V","M","F"],
#     # 3: ["H","V","R","S","L","Q"],
#     # 4: ["F","S","V","Q","P","M","T","J"],
#     # 5: ["L","S","W"],
#     # 6: ["F","V","P","M","R","J","W"],
#     # 7: ["J","Q","C","P","N","R","F"],
#     # 8: ["V","H","P","S","Z","W","R","B"],
#     # 9: ["B","M","J","C","G","H","Z","W"],
# }

crates = defaultdict(list)
moves = []

def getTopCrates(crates):
    top = []

    for stack in crates.values():
        if len(stack) > 0:
            top.append(stack[-1])
    
    return top

def applyMoves(crates, moves):
    for move in moves:
        numCrates, fromStackIdx, toStackIdx = move
        fromStack = crates[fromStackIdx]
        toStack = crates[toStackIdx]

        toStack.extend(fromStack[len(fromStack) - numCrates:])
        crates[fromStackIdx] = fromStack[:len(fromStack) - numCrates]

def parseCrates(line: str):
    stackNum = 1

    for i in range(0, len(line), 4):
        potentialCrate = line[i:i+4].strip()

        if len(potentialCrate) == 3:
            crates[stackNum].append(potentialCrate.strip("[]"))

        stackNum += 1

with open('5/input5.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if "move" in strippedLine:
            moves.append([int(x) for x in re.findall(r'\d+', strippedLine)])
        elif len(strippedLine) > 0:
            parseCrates(line)

    f.close()

applyMoves(crates, moves)
print(''.join(getTopCrates(crates)))
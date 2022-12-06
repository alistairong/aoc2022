#!/usr/bin/env python3

import re

crates = {
    1: ["W","M","L","F"],
    2: ["B","Z","V","M","F"],
    3: ["H","V","R","S","L","Q"],
    4: ["F","S","V","Q","P","M","T","J"],
    5: ["L","S","W"],
    6: ["F","V","P","M","R","J","W"],
    7: ["J","Q","C","P","N","R","F"],
    8: ["V","H","P","S","Z","W","R","B"],
    9: ["B","M","J","C","G","H","Z","W"],
}

moves = []

def getTopCrates(crates):
    top = []

    for stack in crates.values():
        if len(stack) > 0:
            top.append(stack[-1])
    
    return top

def applyMoves(crates, moves):
    for move in moves:
        numCrates, fromStack, toStack = move

        for _ in range(int(numCrates)):
            # assume we always have enough crates to move from old stack to new stack
            crate = crates[int(fromStack)].pop()
            crates[int(toStack)].append(crate)

with open('input5.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0 and "move" in strippedLine:
            moves.append(re.findall(r'\d+', strippedLine))

    f.close()

# print(moves)
applyMoves(crates, moves)
print(''.join(getTopCrates(crates)))
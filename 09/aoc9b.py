#!/usr/bin/env python3

import math

# calculate the grid size by keeping track of max offset of LR and UD
# next, trace outline of tail, and put a 1 if the tail visits that position
# sum up all 1s in the grid

moves = []

def formGrid(moves: list[int]) -> list[list[int]]:
    maxL = 0
    maxR = 0
    maxU = 0
    maxD = 0
    offsetLR = 0
    offsetUD = 0

    for move in moves:
        direction, numSteps = move

        match direction:
            case "L":
                offsetLR -= numSteps
                
                if offsetLR < maxL:
                    maxL = offsetLR
            case "R":
                offsetLR += numSteps
                
                if offsetLR > maxR:
                    maxR = offsetLR
            case "U":
                offsetUD -= numSteps
                
                if offsetUD < maxU:
                    maxU = offsetUD
            case "D":
                offsetUD += numSteps
                
                if offsetUD > maxD:
                    maxD = offsetUD

    numRows = maxD - maxU + 1 # add the starting position
    numCols = maxR - maxL + 1

    return [[0 for _ in range(numCols)] for _ in range(numRows)]

def moveBody(body, newHead):
    body[0] = newHead

    for i in range(1, len(body)):
        headRowIdx, headColIdx = body[i-1]
        tailRowIdx, tailColIdx = body[i]

        diffRow = headRowIdx - tailRowIdx
        diffCol = headColIdx - tailColIdx

        if abs(diffRow) == 2:
            tailRowIdx += 1 if diffRow > 0 else -1 

            if abs(diffCol) == 1:
                tailColIdx += diffCol
        if abs(diffCol) == 2:
            tailColIdx += 1 if diffCol > 0 else - 1

            if abs(diffRow) == 1:
                tailRowIdx += diffRow

        body[i] = (tailRowIdx, tailColIdx)

    return body

def getNumTailPositions(moves, grid):
    # mark everything except for the head position as being visited by tail
    bodyPositions = [(0,0) for _ in range(10)]

    # mark start
    grid[0][0] = 1

    for move in moves:
        direction, numSteps = move

        while numSteps > 0:
            numSteps -= 1
            headRowIdx, headColIdx = bodyPositions[0]

            match direction:
                case "L":
                    headColIdx -= 1
                case "R":
                    headColIdx += 1
                case "U":
                    headRowIdx -= 1
                case "D":
                    headRowIdx += 1

            bodyPositions = moveBody(
                bodyPositions, (headRowIdx, headColIdx))

            tailRowIdx, tailColIdx = bodyPositions[-1]
            grid[tailRowIdx][tailColIdx] = 1
        
        # print(bodyPositions)

    return sum([sum(row) for row in grid])

with open('9/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            direction, numSteps = strippedLine.split(" ")
            moves.append((direction, int(numSteps)))

    f.close()

grid = formGrid(moves)
print(getNumTailPositions(moves, grid))
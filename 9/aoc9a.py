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

def getNumTailPositions(moves, grid):
    # mark everything except for the head position as being visited by tail
    tailRowIdx = 0
    tailColIdx = 0
    headRowIdx = 0
    headColIdx = 0

    # mark start
    grid[tailRowIdx][tailColIdx] = 1

    for move in moves:
        direction, numSteps = move

        match direction:
            case "L":
                while numSteps > 0:
                    numSteps -= 1
                    headColIdx -= 1

                    if abs(headColIdx - tailColIdx) == 2:
                        tailRowIdx = headRowIdx
                        tailColIdx = headColIdx + 1
                        grid[tailRowIdx][tailColIdx] = 1
            case "R":
                while numSteps > 0:
                    numSteps -= 1
                    headColIdx += 1

                    if abs(headColIdx - tailColIdx) == 2:
                        tailRowIdx = headRowIdx
                        tailColIdx = headColIdx - 1
                        grid[tailRowIdx][tailColIdx] = 1
            case "U":
                while numSteps > 0:
                    numSteps -= 1
                    headRowIdx -= 1

                    if abs(headRowIdx - tailRowIdx) == 2:
                        tailRowIdx = headRowIdx + 1
                        tailColIdx = headColIdx
                        grid[tailRowIdx][tailColIdx] = 1
            case "D":
                while numSteps > 0:
                    numSteps -= 1
                    headRowIdx += 1

                    if abs(headRowIdx - tailRowIdx) == 2:
                        tailRowIdx = headRowIdx - 1
                        tailColIdx = headColIdx
                        grid[tailRowIdx][tailColIdx] = 1

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
#!/usr/bin/env python3

import math

# store everything in an n by n grid
# for left, right, up, down, store stack of highest height so far, to know how many trees it can see
# multiply left, right, up, down in the scenic score map for each tree

forest = []

def getScenicScoreMap(forest: list[list[int]]) -> list[list[int]]:
    scenicScoreMap = [[1 for _ in range(len(forest[0]))] for _ in range(len(forest))]
    
    for rowIdx, row in enumerate(forest):
        # from left
        heightStack = [(math.inf, 0)]
        for colIdx, height in enumerate(row):
            while len(heightStack) > 0:
                prevHeight, prevIdx = heightStack[-1]

                if height > prevHeight:
                    heightStack.pop()
                    continue
                else:
                    scenicScoreMap[rowIdx][colIdx] *= (colIdx - prevIdx)
                    heightStack.append((height, colIdx))
                    break
        
        # from right
        heightStack = [(math.inf, len(row) - 1)]
        for colIdx in range(len(row) - 1, -1, -1):
            height = row[colIdx]
            while len(heightStack) > 0:
                prevHeight, prevIdx = heightStack[-1]

                if height > prevHeight:
                    heightStack.pop()
                    continue
                else:
                    scenicScoreMap[rowIdx][colIdx] *= (prevIdx - colIdx)
                    heightStack.append((height, colIdx))
                    break
    
    for colIdx in range(len(forest[0])):
        # from top
        heightStack = [(math.inf, 0)]
        for rowIdx in range(len(forest)):
            height = forest[rowIdx][colIdx]
            while len(heightStack) > 0:
                prevHeight, prevIdx = heightStack[-1]

                if height > prevHeight:
                    heightStack.pop()
                    continue
                else:
                    scenicScoreMap[rowIdx][colIdx] *= (rowIdx - prevIdx)
                    heightStack.append((height, rowIdx))
                    break

        # from bottom
        heightStack = [(math.inf, len(forest) - 1)]
        for rowIdx in range(len(forest) - 1, -1, -1):
            height = forest[rowIdx][colIdx]
            while len(heightStack) > 0:
                prevHeight, prevIdx = heightStack[-1]

                if height > prevHeight:
                    heightStack.pop()
                    continue
                else:
                    scenicScoreMap[rowIdx][colIdx] *= (prevIdx - rowIdx)
                    heightStack.append((height, rowIdx))
                    break

    return scenicScoreMap

def getHighestScenicScore(scenicScoreMap: list[list[int]]) -> int:
    return max([max(row) for row in scenicScoreMap])

with open('8/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            forest.append([int(height) for height in strippedLine])

    f.close()

print(getHighestScenicScore(getScenicScoreMap(forest)))
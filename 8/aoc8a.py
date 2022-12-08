#!/usr/bin/env python3

# store everything in an n by n grid
# for left, right, up, down, if tree is taller than the prev, it can be seen
# if reach 9 (tallest height of tree), we can short circuit stop looking down that row / col
# keep a grid record of whether each tree can be seen
# get sum of all trees that can be seen

forest = []
maxHeight = 9

def getVisibleTrees(forest: list[list[int]]) -> int:
    visibilityMap = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
    
    for rowIdx, row in enumerate(forest):
        # from left
        edgeHeight = -1
        for colIdx, height in enumerate(row):
            if height > edgeHeight:
                visibilityMap[rowIdx][colIdx] = 1
                edgeHeight = height
            
            # short circuit if we reach tallest height
            if height == maxHeight:
                break  
        
        # from right
        edgeHeight = -1
        for colIdx in range(len(row) - 1, -1, -1):
            height = row[colIdx]
            if height > edgeHeight:
                visibilityMap[rowIdx][colIdx] = 1
                edgeHeight = height
            
            # short circuit if we reach tallest height
            if height == maxHeight:
                break  
    
    for colIdx in range(len(forest[0])):
        # from top
        edgeHeight = -1
        for rowIdx in range(len(forest)):
            height = forest[rowIdx][colIdx]
            if height > edgeHeight:
                visibilityMap[rowIdx][colIdx] = 1
                edgeHeight = height
            
            # short circuit if we reach tallest height
            if height == maxHeight:
                break

        # from bottom
        edgeHeight = -1
        for rowIdx in range(len(forest) - 1, -1, -1):
            height = forest[rowIdx][colIdx]
            if height > edgeHeight:
                visibilityMap[rowIdx][colIdx] = 1
                edgeHeight = height
            
            # short circuit if we reach tallest height
            if height == maxHeight:
                break

    return sum([sum(row) for row in visibilityMap])

with open('8/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            forest.append([int(height) for height in strippedLine])

    f.close()

# print(forest)
print(getVisibleTrees(forest))
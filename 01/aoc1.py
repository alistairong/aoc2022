#!/usr/bin/env python3

globalMax = 0
currMax = 0
allWeights = []

with open('input1.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()
        if len(strippedLine) == 0:
            # globalMax = max(currMax, globalMax)
            allWeights.append(currMax)
            currMax = 0
        else:
            currMax += int(strippedLine)

    f.close()

allWeights.sort()
print(allWeights[-1]+allWeights[-2]+allWeights[-3])
print(allWeights)
# print(globalMax)
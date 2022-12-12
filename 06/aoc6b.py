#!/usr/bin/env python3

from collections import Counter

numDistinct = 14

def findMarker(line: str) -> int:
    # start-of-packet marker consists of 14 distinct characters
    countMap = Counter(line[:numDistinct-1])

    for end in range(numDistinct-1, len(line)):
        letter = line[end]
        countMap[letter] += 1

        if max(countMap.values()) < 2:
            # end + 1th element for conversion from 0 index to 1 index
            return end + 1
        
        start = end - (numDistinct - 1)
        startLetter = line[start]
        countMap[startLetter] -= 1

with open('6/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        print(findMarker(strippedLine))

    f.close()
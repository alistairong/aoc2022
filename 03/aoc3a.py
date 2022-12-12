#!/usr/bin/env python3

from collections import Counter

def getPriorityElem(line):
  midPt = int(len(line) / 2)
  firstHalfMap = Counter(line[:midPt])
  secondHalfMap = Counter(line[midPt:])

  firstHalfSet = set(firstHalfMap.keys())
  secondHalfSet = set(secondHalfMap.keys())

  intersection = firstHalfSet & secondHalfSet

  for elem in intersection:
    return elem


def getPriorityScore(elem):
  if ord(elem) - ord('a') < 0:
    return ord(elem) - ord('A') + 27
  
  return ord(elem) - ord('a') + 1

sum = 0

with open('input3.txt') as f:
  for line in f.readlines():
    strippedLine = line.strip()
  
    if len(strippedLine):
      letter = getPriorityElem(strippedLine)
      sum += getPriorityScore(letter)
  
  f.close()

print(sum)
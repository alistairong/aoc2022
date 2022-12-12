#!/usr/bin/env python3

from collections import Counter

def getPriorityElem(lines):
  intersection = set()

  for line in lines:
    letterSet = set(Counter(line).keys())

    if len(intersection) == 0:
      intersection = letterSet
    else:
      intersection = intersection & letterSet
  
  for elem in intersection:
    return elem


def getPriorityScore(elem):
  if ord(elem) - ord('a') < 0:
    return ord(elem) - ord('A') + 27
  
  return ord(elem) - ord('a') + 1

lines = []
sum = 0

with open('input3.txt') as f:
  for line in f.readlines():
    strippedLine = line.strip()
  
    if len(strippedLine):
      lines.append(strippedLine)
  
  f.close()

for i in range(0, len(lines), 3):
  letter = getPriorityElem(lines[i:i+3])
  sum += getPriorityScore(letter)

print(sum)
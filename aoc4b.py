#!/usr/bin/env python3

from collections import Counter

def checkRangeOverlaps(firstStart, firstEnd, secondStart, secondEnd):
  # first range to always be the bigger range / starts first
  # swap if this is not the case
  if firstStart > secondStart or (firstStart == secondStart and secondEnd > firstEnd):
    firstStart, firstEnd, secondStart, secondEnd = secondStart, secondEnd, firstStart, firstEnd
  
  if firstStart <= secondStart and firstEnd >= secondStart:
    return True

  return False

lines = []
sum = 0

with open('input4.txt') as f:
  for line in f.readlines():
    strippedLine = line.strip()
  
    if len(strippedLine):
      lines.append(strippedLine)
  
  f.close()

for line in lines:
  first, second = line.split(",")

  firstStart, firstEnd = first.split("-")
  secondStart, secondEnd = second.split("-")

  if checkRangeOverlaps(int(firstStart), int(firstEnd), int(secondStart), int(secondEnd)):
    sum += 1

print(sum)
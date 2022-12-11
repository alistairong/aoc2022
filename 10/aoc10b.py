#!/usr/bin/env python3

import math

instructions = []
drawing = [['.' for _ in range(40)] for _ in range(6)]

def getRowColIdx(cycleIdx):
    col = cycleIdx % 40
    row = int(cycleIdx / 40)

    return row, col

def drawImage(instructions):
    regValue = 0
    cycleIdx = 0

    for instruction in instructions:
        row, col = getRowColIdx(cycleIdx)
        if regValue == col or regValue + 1 == col or regValue + 2 == col:
            drawing[row][col] = '#'

        cycleIdx += 1
        match len(instruction):
            case 1:
                # noop
                continue
            case 2:
                row, col = getRowColIdx(cycleIdx)
                if regValue == col or regValue + 1 == col or regValue + 2 == col:
                    drawing[row][col] = '#'

                _, val = instruction
                cycleIdx += 1
                regValue += int(val)

def printDrawing():
    for line in drawing:
        print(line)

with open('10/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            instructions.append(strippedLine.split())

    f.close()

drawImage(instructions)
printDrawing()
#!/usr/bin/env python3

import math

instructions = []
cycles = [20, 60, 100, 140, 180, 220]

def sumSignalStrength(instructions, cycles):
    total = 0
    regValue = 1
    cycleIdx = 1

    cycleStack = list(reversed(cycles))

    for instruction in instructions:
        if cycleStack[-1] == cycleIdx:
            total += regValue * cycleIdx
            cycleStack.pop()
        
        if len(cycleStack) == 0:
            break

        cycleIdx += 1
        match len(instruction):
            case 1:
                # noop
                continue
            case 2:
                if cycleStack[-1] == cycleIdx:
                    total += regValue * cycleIdx
                    cycleStack.pop()

                if len(cycleStack) == 0:
                    break
                
                _, val = instruction
                cycleIdx += 1
                regValue += int(val)
    
    return total


with open('10/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            instructions.append(strippedLine.split())

    f.close()

print(sumSignalStrength(instructions, cycles))

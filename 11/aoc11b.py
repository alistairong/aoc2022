#!/usr/bin/env python3

from dataclasses import dataclass, field
import re
import math
from collections import deque

linesPerMonkey = 6

@dataclass
class Monkey:
    id: int = 0
    items: deque[int] = field(default_factory=deque, init=True) # [itemID1, itemID2....]
    op: str = ""
    opVar: int = math.inf
    div: int = 1
    trueID: int = 0
    falseID: int = 0

def parseLines(lines: list[str]) -> list[Monkey]:
    monkeys: list[Monkey] = []
    monkey = Monkey()

    for lineNum, line in enumerate(lines):
        # for every 6 lines save it as 1 monkey
        lineVars = line.split()

        match lineNum % linesPerMonkey:
            case 0:
                monkey.id = int(lineVars[-1].strip(":"))
            case 1:
                items = deque([int(x) for x in re.findall(r'\d+', line)])
                monkey.items = items
            case 2:
                op, opVar = lineVars[len(lineVars) - 2:]
                monkey.op = op
                monkey.opVar = math.inf if opVar == "old" else int(opVar)
            case 3:
                div = int(lineVars[-1])
                monkey.div = div
            case 4:
                trueMonkeyID = int(lineVars[-1])
                monkey.trueID = trueMonkeyID
            case 5:
                falseMonkeyID = int(lineVars[-1])
                monkey.falseID = falseMonkeyID

                monkeys.append(monkey)

                monkey = Monkey()

    return monkeys

# simulateRounds returns list of number of items each monkey has inspected after "rounds" number of rounds.
def simulateRounds(monkeys: list[Monkey], rounds: int) -> list[int]:
    monkeyActions = [0 for _ in range(len(monkeys))]

    # to reduce the item worry level to a more calculatable number
    # THIS IS THE MAGIC SAUCE TO MAKE IT FASTER IN CALCULATING 
    # (hint was that we needed to find another way to reduce worry levels)
    monkeyDivProd = math.prod([monkey.div for monkey in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            numItems = len(monkey.items)

            if numItems == 0:
                continue

            monkeyActions[monkey.id] += numItems

            for _ in range(numItems):
                item = monkey.items.popleft()
                opVar = item if monkey.opVar == math.inf else monkey.opVar
                
                match monkey.op:
                    case '+':
                        item += opVar
                    case '*':
                        item *= opVar
                
                item = item % monkeyDivProd

                if item % monkey.div == 0:
                    monkeys[monkey.trueID].items.append(item)
                else:
                    monkeys[monkey.falseID].items.append(item)

    return monkeyActions

def calculateMonkeyBusiness(monkeyActions: list[int]) -> int:
    sortedList = sorted(monkeyActions)
    return sortedList[-1] * sortedList[-2]

lines = []

with open('11/input.txt') as f:
    for line in f.readlines():
        strippedLine = line.strip()

        if len(strippedLine) > 0:
            lines.append(strippedLine)

    f.close()

monkeys = parseLines(lines)
monkeyActions = simulateRounds(monkeys, 10000)
print(calculateMonkeyBusiness(monkeyActions))

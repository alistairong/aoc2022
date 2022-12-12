#!/usr/bin/env python3

from dataclasses import dataclass, field
import re
from collections import deque

linesPerMonkey = 6

@dataclass
class Monkey:
    id: int = 0
    items: deque[int] = field(default_factory=deque, init=True) # [itemID1, itemID2....]
    operation: list[any] = field(default_factory=list, init=True) # [operation, amt]
    testVars: list[int] = field(default_factory=list, init=True) # [amt, trueMonkeyID, falseMonkeyID]

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
                operation = lineVars[len(lineVars) - 2:]
                monkey.operation = operation
            case 3:
                testAmt = int(lineVars[-1])
                monkey.testVars.append(testAmt)
            case 4:
                trueMonkeyID = int(lineVars[-1])
                monkey.testVars.append(trueMonkeyID)
            case 5:
                falseMonkeyID = int(lineVars[-1])
                monkey.testVars.append(falseMonkeyID)

                monkeys.append(monkey)

                monkey = Monkey()

    return monkeys

# simulateRounds returns list of number of items each monkey has inspected after "rounds" number of rounds.
def simulateRounds(monkeys: list[Monkey], rounds: int) -> list[int]:
    monkeyActions = [0 for _ in range(len(monkeys))]

    for _ in range(rounds):
        for monkey in monkeys:
            numItems = len(monkey.items)

            if numItems == 0:
                continue

            monkeyActions[monkey.id] += numItems

            for _ in range(numItems):
                item = monkey.items.popleft()
                op, strOpVar = monkey.operation
                opVar = 0

                if strOpVar == "old":
                    opVar = item
                elif strOpVar.isdigit():
                    opVar = int(strOpVar)
                
                match op:
                    case '+':
                        item += opVar
                    case '*':
                        item *= opVar
                
                item = int(item / 3)
                testVar, trueMonkeyID, falseMonkeyID = monkey.testVars

                if item % testVar == 0:
                    monkeys[trueMonkeyID].items.append(item)
                else:
                    monkeys[falseMonkeyID].items.append(item)

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
monkeyActions = simulateRounds(monkeys, 20)
print(calculateMonkeyBusiness(monkeyActions))

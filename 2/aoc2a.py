#!/usr/bin/env python3

def getMoveScore(oppMove, selfMove):
  score = 0

  match selfMove:
    case "X":
      score += 1

      match oppMove:
        case "A":
          score += 3
        case "C":
          score += 6
    case "Y":
      score += 2

      match oppMove:
        case "A":
          score += 6
        case "B":
          score += 3
    case "Z":
      score += 3

      match oppMove:
        case "B":
          score += 6
        case "C":
          score += 3

  return score

scores = []

with open('input2.txt') as f:
  for line in f.readlines():
    strippedLine = line.strip()

    if len(strippedLine):
      oppMove, selfMove = strippedLine.split(' ')
      print(oppMove,selfMove)

      score = getMoveScore(oppMove, selfMove)
      scores.append(score)
  
  f.close()

print(sum(scores))

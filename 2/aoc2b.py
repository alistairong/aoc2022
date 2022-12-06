#!/usr/bin/env python3

def getMoveScore(oppMove, selfMove):
  score = 0

  match selfMove:
    case "X":
      match oppMove:
        case "A":
          score += 3
        case "B":
          score += 1
        case "C":
          score += 2
    case "Y":
      score += 3

      match oppMove:
        case "A":
          score += 1
        case "B":
          score += 2
        case "C":
          score += 3
    case "Z":
      score += 6

      match oppMove:
        case "A":
          score += 2
        case "B":
          score += 3
        case "C":
          score += 1

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

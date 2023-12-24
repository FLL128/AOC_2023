import math
from functools import reduce

file = open("input.txt","r")
parts = file.read().split("\n\n")

# Part 1
directions = parts[0]
moves = parts[1].split("\n")
place = "AAA"
i = 0
steps = 0
while place[2] != "Z":
    for move in moves:
        if move.split()[0] == place:
            if i<len(directions):
                if directions[i] == "L": place = move.split()[2][1:-1]
                else: place = move.split()[3][:-1]
                i+=1
                steps+=1
                break
            else:
                i=0
                if directions[i] == "L": place = move.split()[2][1:-1]
                else: place = move.split()[3][:-1]
                i+=1
                steps+=1
                break
print(steps)

# Part 2
candidates = []
for line in moves:
    if line.split()[0][2]=="A":
        candidates.append(line)

max_steps = []
for line in candidates:
    counter = 0
    if line.split()[0][2]=="A":
        place = line.split()[0]
        cur_steps = 0
        i = 0
        while place[2] != "Z":
            for move in moves:
                if move.split()[0] == place:
                    if i<len(directions):
                        if directions[i] == "L": place = move.split()[2][1:-1]
                        else: place = move.split()[3][:-1]
                        i+=1
                        cur_steps+=1
                        break
                    else:
                        i=0
                        if directions[i] == "L": place = move.split()[2][1:-1]
                        else: place = move.split()[3][:-1]
                        i+=1
                        cur_steps+=1
                        break
        max_steps.append(cur_steps)
print(reduce(math.lcm, max_steps))
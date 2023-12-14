import functools


file = open("input.txt","r")
lines = file.read().split("\n")
new_lines = lines.copy()
# Part 1
total = 0
for i in range(len(lines)):
    lines[i] = list(lines[i])
    for j in range(len(lines[0])):
        if lines[i][j]=="O":
            x = i-1
            while x>=0 and lines[x][j]==".":
                lines[x][j]="O"
                lines[x+1][j]="."
                x-=1
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=="O":
            total += len(lines)-i
print(total)

# Part 2
lines = new_lines
@functools.cache
def turn(lines):
    lines = list(lines)
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]=="O":
                x = i-1
                while x>=0 and lines[x][j]==".":
                    lines[x][j]="O"
                    lines[x+1][j]="."
                    x-=1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]=="O":
                x = j-1
                while x>=0 and lines[i][x]==".":
                    lines[i][x]="O"
                    lines[i][x+1]="."
                    x-=1
    for i in range(len(lines)-1,-1,-1):
        for j in range(len(lines[0])):
            if lines[i][j]=="O":
                x = i+1
                while x<len(lines) and lines[x][j]==".":
                    lines[x][j]="O"
                    lines[x-1][j]="."
                    x+=1
    for i in range(len(lines)):
        for j in range(len(lines[0])-1,-1,-1):
            if lines[i][j]=="O":
                x = j+1
                while x<len(lines[0]) and lines[i][x]==".":
                    lines[i][x]="O"
                    lines[i][x-1]="."
                    x+=1
    for i in range(len(lines)):
        lines[i] = "".join(lines[i])
    return tuple(lines)

@functools.cache
def outer(lines):
    for i in range(10000):
        lines = turn(lines)
    return lines

# Yes, I could save them and check for loops, but why do that when you can just tell python to cache it :D
lines = tuple(lines)
for z in range(100000):
    lines = outer(lines)
        
total = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=="O":
            total += len(lines)-i
print(total)
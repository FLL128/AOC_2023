file = open("input.txt","r")
lines = file.read().split("\n")

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

patterns = []
i = 0
lines = tuple(lines)
while lines not in patterns:
    patterns.append(lines)
    lines = turn(lines)
    i+=1
start = patterns.index(lines)
lines = patterns[(1000000000-start)%(i-start)+start]
total = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=="O":
            total += len(lines)-i
print(total)
file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
for i in range(len(lines)):
    lines[i] = list(lines[i])
    if not "#" in lines[i]:
        for j in range(len(lines[i])):
            lines[i][j]="o"

for j in range(len(lines[0])):
    line = []
    for i in range(len(lines)):
        line.append(lines[i][j])
    if not "#" in line: 
        for i in range(len(lines)):
            lines[i][j]="o"
    
galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            galaxies.append([i,j])

total = 0
for i in galaxies:
    for j in galaxies:
        if i!=j:
            start = min(i[0],j[0])
            end = max(i[0],j[0])
            for x in range(start,end):
                if lines[x][0]=="o": total += 2
                else: total += 1
            start = min(i[1],j[1])
            end = max(i[1],j[1])
            for y in range(start,end):
                if lines[0][y]=="o": total += 2
                else: total += 1
print(int(total/2))

# Part 2
total = 0
for i in galaxies:
    for j in galaxies:
        if i!=j:
            start = min(i[0],j[0])
            end = max(i[0],j[0])
            for x in range(start,end):
                if lines[x][0]=="o": total += 1000000
                else: total += 1
            start = min(i[1],j[1])
            end = max(i[1],j[1])
            for y in range(start,end):
                if lines[0][y]=="o": total += 1000000
                else: total += 1         
print(int(total/2))
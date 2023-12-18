file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
grid = []
for i in range(1000):
    cur = []
    for j in range(1000):
        cur.append(".")
    grid.append(cur)
x = 500
y = 500
total = 0

for line in lines:
    line = line.split()
    if line[0]=="U":
        for i in range(int(line[1])):
            x-=1
            grid[x][y] = "#"
    elif line[0]=="D":
        for i in range(int(line[1])):
            x+=1
            grid[x][y] = "#"
    elif line[0]=="L":
        for i in range(int(line[1])):
            y-=1
            grid[x][y] = "#"
    elif line[0]=="R":
        for i in range(int(line[1])):
            y+=1
            grid[x][y] = "#"

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="#": total+=1

# Copy from Day10 solution
for i in range(len(grid)):
    j=0
    pr = False
    while j<len(grid[0]):
        if grid[i][j]=="#":
            a=grid[i-1][j]+grid[i+1][j]
            while grid[i][j]=="#": j+=1
            b=grid[i-1][j-1]+grid[i+1][j-1]
            if a[0]=="#"==b[1] or a[1]=="#"==b[0]:
                pr = not pr
            j=j-1
        elif pr:
            total += 1
        j+=1
print(total)

# Part 2
total = 1
y = 1
for line in lines:
    line = line.split()
    dist = int(line[2][2:7],base=16)
    direc = int(line[2][-2])
    if direc==0:
        y += dist
        total += dist
    elif direc==1:
        total += (y+1)*dist
    elif direc==2:
        y -= dist
    elif direc==3:
        total -= y*dist
print(total)
import heapq

file = open("input.txt","r")
grid = file.read().split("\n")

# Part 1
x = 0
y = 0
for i,line in enumerate(grid):
    grid[i] = list(line)
    for j,e in enumerate(line):
        if e=="S":
            x=i
            y=j

def addNeighbours(cur):
    depth,x,y = cur
    # Add straight
    if x-2>=0 and grid[x-1][y] not in "#" and grid[x-2][y] not in "#O":
        grid[x-2][y]="O"
        queue.append((depth+2,x-2,y))
    if y-2>=0 and grid[x][y-1] not in "#" and grid[x][y-2] not in "#O":
        grid[x][y-2]="O"
        queue.append((depth+2,x,y-2))
    if x+2<len(grid) and grid[x+1][y] not in "#" and grid[x+2][y] not in "#O":
        grid[x+2][y]="O"
        queue.append((depth+2,x+2,y))
    if y+2<len(grid[0]) and grid[x][y+1] not in "#" and grid[x][y+2] not in "#O":
        grid[x][y+2]="O"
        queue.append((depth+2,x,y+2))
    # Add diagonally
    if x-1>=0 and y-1>=0 and grid[x-1][y]+grid[x][y-1] not in "##" and grid[x-1][y-1] not in "#O":
        grid[x-1][y-1]="O"
        queue.append((depth+2,x-1,y-1))
    if x-1>=0 and y+1<len(grid[0]) and grid[x-1][y]+grid[x][y+1] not in "##" and grid[x-1][y+1] not in "#O":
        grid[x-1][y+1]="O"
        queue.append((depth+2,x-1,y+1))
    if x+1<len(grid) and y-1>=0 and grid[x+1][y]+grid[x][y-1] not in "##" and grid[x+1][y-1] not in "#O":
        grid[x+1][y-1]="O"
        queue.append((depth+2,x+1,y-1))
    if x+1<len(grid) and y+1<len(grid[0])  and grid[x+1][y]+grid[x][y+1] not in "##" and grid[x+1][y+1] not in "#O":
        grid[x+1][y+1]="O"
        queue.append((depth+2,x+1,y+1))      
queue = [(0,x,y)]
depth = 0
while True:
    cur = heapq.heappop(queue)
    if cur[0]>=64: break
    addNeighbours(cur)

total=0
for line in (grid):
    for e in (line):
        if e=="O":
            total += 1
print(total)

# Part 2
# 26501365 steps
print(26501365/65)
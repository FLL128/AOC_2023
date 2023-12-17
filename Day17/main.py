import heapq

file = open("input.txt","r")
grid = file.read().split("\n")

# Part 1
def addNeighbours(a,x,y,c,direc):
    if x>0 and (direc,c) not in visited[x-1][y]:
        if direc != "u":
            queue.append((a+grid[x-1][y],x-1,y,1,"u"))
            visited[x-1][y]+=(direc,c)
        elif c<3:
            queue.append((a+grid[x-1][y],x-1,y,c+1,"u"))
            visited[x-1][y].append((direc,c))
    if x<len(grid)-1 and (direc,c) not in visited[x+1][y]:
        if direc != "d":
            queue.append((a+grid[x+1][y],x+1,y,1,"d"))
            visited[x+1][y].append((direc,c))
        elif c<3:
            queue.append((a+grid[x+1][y],x+1,y,c+1,"d"))
            visited[x+1][y].append((direc,c))
    if y>0 and (direc,c) not in visited[x][y-1]:
        if direc != "l":
            queue.append((a+grid[x][y-1],x,y-1,1,"l"))
            visited[x][y-1].append((direc,c))
        elif c<3:
            queue.append((a+grid[x][y-1],x,y-1,c+1,"l"))
            visited[x][y-1].append((direc,c))
    if y<len(grid[0])-1 and (direc,c) not in visited[x][y+1]:
        if direc != "r":
            queue.append((a+grid[x][y+1],x,y+1,1,"r"))
            visited[x][y+1].append((direc,c))
        elif c<3:
            queue.append((a+grid[x][y+1],x,y+1,c+1,"r"))
            visited[x][y+1].append((direc,c))
x = 0
y = 0
visited = []
for i in range(len(grid)):
    cur=[]
    grid[i] = list(grid[i])
    for j in range(len(grid[0])):
        cur.append([])
        grid[i][j] = int(grid[i][j])
    visited.append(cur)
a=0
queue = [(0,0,0,1,"r")]
while (x!= len(grid)-1 or y!= len(grid[0])-1):
    cur = heapq.heappop(queue)
    a = cur[0]
    x = cur[1]
    y = cur[2]
    addNeighbours(a,x,y,cur[3],cur[4])
print(a)

# Part 2
def addNeighboursTwo(a,x,y,c,direc):
    if direc=="u" and c<4:
        if x>0 and (direc,c) not in visited[x-1][y]:
            queue.append((a+grid[x-1][y],x-1,y,c+1,"u"))
            visited[x-1][y]+=(direc,c)
        return
    elif direc=="d" and c<4:
        if x<len(grid)-1 and (direc,c) not in visited[x+1][y]:
            queue.append((a+grid[x+1][y],x+1,y,c+1,"d"))
            visited[x+1][y]+=(direc,c)
        return
    elif direc=="l" and c<4:
        if y>0 and (direc,c) not in visited[x][y-1]:
            queue.append((a+grid[x][y-1],x,y-1,c+1,"l"))
            visited[x][y-1]+=(direc,c)
        return
    elif direc=="r" and c<4:
        if y<len(grid[0])-1 and (direc,c) not in visited[x][y+1]:
            queue.append((a+grid[x][y+1],x,y+1,c+1,"r"))
            visited[x][y+1]+=(direc,c)
        return    
    if x>0 and (direc,c) not in visited[x-1][y]:
        if direc != "u":
            queue.append((a+grid[x-1][y],x-1,y,1,"u"))
            visited[x-1][y]+=(direc,c)
        elif c<10:
            queue.append((a+grid[x-1][y],x-1,y,c+1,"u"))
            visited[x-1][y].append((direc,c))
    if x<len(grid)-1 and (direc,c) not in visited[x+1][y]:
        if direc != "d":
            queue.append((a+grid[x+1][y],x+1,y,1,"d"))
            visited[x+1][y].append((direc,c))
        elif c<10:
            queue.append((a+grid[x+1][y],x+1,y,c+1,"d"))
            visited[x+1][y].append((direc,c))
    if y>0 and (direc,c) not in visited[x][y-1]:
        if direc != "l":
            queue.append((a+grid[x][y-1],x,y-1,1,"l"))
            visited[x][y-1].append((direc,c))
        elif c<10:
            queue.append((a+grid[x][y-1],x,y-1,c+1,"l"))
            visited[x][y-1].append((direc,c))
    if y<len(grid[0])-1 and (direc,c) not in visited[x][y+1]:
        if direc != "r":
            queue.append((a+grid[x][y+1],x,y+1,1,"r"))
            visited[x][y+1].append((direc,c))
        elif c<10:
            queue.append((a+grid[x][y+1],x,y+1,c+1,"r"))
            visited[x][y+1].append((direc,c))

x = 0
y = 0
visited = []
for i in range(len(grid)):
    cur=[]
    grid[i] = list(grid[i])
    for j in range(len(grid[0])):
        cur.append([])
        grid[i][j] = int(grid[i][j])
    visited.append(cur)
a=0
queue = [(0,0,0,1,"r")]
while (x!= len(grid)-1 or y!= len(grid[0])-1):
    cur = heapq.heappop(queue)
    a = cur[0]
    x = cur[1]
    y = cur[2]
    addNeighboursTwo(a,x,y,cur[3],cur[4])
print(a)
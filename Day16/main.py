import sys

sys.setrecursionlimit(2000)
file = open("input.txt","r")
grid = file.read().split("\n")

# Part 1
passed = []
for i in range(len(grid)):
    cur=[]
    for j in range(len(grid[0])):
        cur.append(False)
    passed.append(cur)
known = set({})

def beam(x,y,d):
    if (x,y,d) in known: return
    known.add((x,y,d))
    if 0<=y<len(grid[0]) and 0<=x<len(grid): passed[x][y]=True
    else: return  
    if d=="r" and y<len(grid[0]):
        if grid[x][y]=='/': beam(x-1,y,'u')
        elif grid[x][y]=='\\': beam(x+1,y,'d')
        elif grid[x][y]=='|': 
            beam(x-1,y,'u')
            beam(x+1,y,'d')
        else: 
            y+=1
            while y<len(grid[0]) and grid[x][y] in ".-":
                passed[x][y]=True
                known.add((x,y,d))
                y+=1
            beam(x,y,d)
    elif d=="l" and y>=0:
        if grid[x][y]=='/': beam(x+1,y,'d')
        elif grid[x][y]=='\\': beam(x-1,y,'u')
        elif grid[x][y]=='|': 
            beam(x+1,y,'d')
            beam(x-1,y,'u')
        else:
            y-=1
            while y>=0 and grid[x][y] in ".-":
                passed[x][y]=True
                known.add((x,y,d))
                y-=1
            beam(x,y,d)
    elif d=="u" and x>=0:
        if grid[x][y]=='/': beam(x,y+1,'r')
        elif grid[x][y]=='\\': beam(x,y-1,'l')
        elif grid[x][y]=='-': 
            beam(x,y+1,'r')
            beam(x,y-1,'l')
        else:
            x-=1
            while x>=0 and grid[x][y] in ".|":
                passed[x][y]=True
                known.add((x,y,d))
                x-=1
            beam(x,y,d)
    elif d=="d" and x<len(grid):
        if grid[x][y]=='/': beam(x,y-1,'l')
        elif grid[x][y]=='\\': beam(x,y+1,'r')
        elif grid[x][y]=='-': 
            beam(x,y-1,'l')
            beam(x,y+1,'r')
        else:
            x+=1
            while x<len(grid) and grid[x][y] in ".|":
                passed[x][y]=True
                known.add((x,y,d))
                x+=1
            beam(x,y,d)

def play(x,y,d):
    global known
    known.clear()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            passed[i][j]=False
    beam(x,y,d)
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if passed[i][j]:
                total += 1
    return total

print(play(0,0,'r'))

# Part 2
best=0
for i in range(len(grid)):
    best = max(play(i,0,'r'),best)
    best = max(play(i,len(grid[0])-1,'l'),best)
for j in range(len(grid[0])):
    best = max(play(0,j,'d'),best)
    best = max(play(len(grid)-1,j,'u'),best)
print(best)

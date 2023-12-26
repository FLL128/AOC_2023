file = open("input.txt","r")
grid = file.read().split("\n")
for i in range(len(grid)):
    grid[i] = list(grid[i])

# Part 1
paths = [(0,1,0,[(0,1)])]
finished_paths = []

while paths != []:
    x,y,length,path = paths.pop(0)
    if x > 0 and grid[x-1][y] in "^." and (x-1,y) not in path:
        paths.append((x-1,y,length+1,[(x,y)]))
    if y > 0 and grid[x][y-1] in "<." and (x,y-1) not in path:
        paths.append((x,y-1,length+1,[(x,y)]))
    if x < len(grid)-1 and grid[x+1][y] in "v." and (x+1,y) not in path:
        if x+1 == len(grid)-1 and y == len(grid[0])-2:
            finished_paths.append(length+1)
        else:
            paths.append((x+1,y,length+1,[(x,y)]))
    if y < len(grid[0])-1 and grid[x][y+1] in ">." and (x,y+1) not in path:
        paths.append((x,y+1,length+1,[(x,y)]))

longest = 0
for path in finished_paths:
    longest = max(longest, path)
print(longest)

# Part 2
paths = [(0,1,0,[(0,1)],(0,1))]
finished_paths = []
storage = []
bla = 0
longest = 0
while paths != [] or storage != []:
    if len(paths) > 1000:
        storage = storage + paths[500:]
        paths = paths[:500]
    elif paths == []:
        paths = storage[:500]
        storage = storage[500:]
        bla = len(storage)
    x,y,length,path,origin = paths.pop(0)
    path = path.copy()
    if x>0 and (grid[x-1][y]+grid[x][y-1]+grid[x+1][y]+grid[x][y+1]).count("#")!=2:
        path.append((x,y))
    if x > 0 and grid[x-1][y] in "^v<>." and (x-1,y) not in path+[origin]:
        paths.append((x-1,y,length+1,path,(x,y)))
    if y > 0 and grid[x][y-1] in "^v<>." and (x,y-1) not in path+[origin]:
        paths.append((x,y-1,length+1,path,(x,y)))
    if x < len(grid)-1 and grid[x+1][y] in "^v<>." and (x+1,y) not in path+[origin]:
        if x+1 == len(grid)-1 and y == len(grid[0])-2:
            finished_paths.append(length+1)
            longest = max(longest, length+1)
            print(longest, len(paths),bla)
        else:
            paths.append((x+1,y,length+1,path,(x,y)))
    if y < len(grid[0])-1 and grid[x][y+1] in "^v<>." and (x,y+1) not in path+[origin]:
        paths.append((x,y+1,length+1,path,(x,y)))
print(len(storage))

print(longest)

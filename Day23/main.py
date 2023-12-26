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
def findPath(start, end):
    x,y = start
    paths = [[x,y,1,(x,y)]]
    while paths != []:
        x,y,length,path = paths.pop(0)
        if x > 0:
            if (x-1,y) == end: return length
            if (x-1,y) != path and grid[x-1][y] == ".":
                paths.append((x-1,y,length+1,(x,y)))
        if y > 0:
            if (x,y-1) == end: return length
            if (x,y-1) != path and grid[x][y-1] == ".":
                paths.append((x,y-1,length+1,(x,y)))
        if x < len(grid)-1:
            if (x+1,y) == end: return length
            if (x+1,y) != path and grid[x+1][y] == ".":
                paths.append((x+1,y,length+1,(x,y)))
        if y < len(grid[0])-1:
            if (x,y+1) == end: return length
            if (x,y+1) != path and grid[x][y+1] == ".":
                paths.append((x,y+1,length+1,(x,y)))
    return 0

# Find all intersections plus start and end point
paths = [(0,1,0,[(0,1)],(0,1))]
intersections = [(0,1),(len(grid)-1, len(grid[0])-2)]
hasPath = [[],[]]
for x in range(1,len(grid)-1):
    for y in range(1,len(grid[0])-1):
        if grid[x][y] == "." and (grid[x-1][y]+grid[x][y-1]+grid[x+1][y]+grid[x][y+1]).count("#")<2:
            intersections.append((x,y))
            grid[x][y]="#"
            hasPath.append([])
        if grid[x][y] in "<>v^":
            grid[x][y] = "."

# Find their distances
for i in range(len(intersections)):
    for j in range(i+1,len(intersections)):
        path = [intersections[i]]
        if len(hasPath[i])<4:
            length = findPath(intersections[i],intersections[j])
            if length!=0:
                hasPath[i].append((j,length))
                hasPath[j].append((i,length))

# Calculate the longest path from start to finish
longest = 0
paths = [[0,0,[0]]]
while paths != []:
    index, length, path = paths.pop()
    if index == 1:
        longest = max(longest,length)
    else:
        for e in hasPath[index]:
            rec, dist = e
            if rec not in path:
                paths.append((rec,length+dist,path+[rec]))
print(longest)

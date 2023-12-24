file = open("input.txt","r")
grid = file.read().split("\n")
for i in range(len(grid)):
    grid[i] = list(grid[i])

# Part 1
paths = [(0,1,[(0,1)])]
finished_paths = []

while paths != []:
    x,y,path = paths.pop(0)
    if x > 0 and grid[x-1][y] in "^." and (x-1,y) not in path:
        paths.append((x-1,y,path+[(x-1,y)]))
    if y > 0 and grid[x][y-1] in "<." and (x,y-1) not in path:
        paths.append((x,y-1,path+[(x,y-1)]))
    if x < len(grid)-1 and grid[x+1][y] in "v." and (x+1,y) not in path:
        if x+1 == len(grid)-1 and y == len(grid[0])-2:
            finished_paths.append((path+[(x+1,y)]))
        else:
            paths.append((x+1,y,path+[(x+1,y)]))
    if y < len(grid[0])-1 and grid[x][y+1] in ">." and (x,y+1) not in path:
        paths.append((x,y+1,path+[(x,y+1)]))

longest = 0
for path in finished_paths:
    longest = max(longest, len(path))
print(longest-1)
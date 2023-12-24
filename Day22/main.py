file = open("input.txt","r")
lines = file.read().split("\n")
# Part 1
bricks = []
for line in lines:
    start = [int(x) for x in line.split("~")[0].split(",")]
    end = [int(x) for x in line.split("~")[1].split(",")]
    bricks.append((start,end))
grid = []
for i in range(10):
    plane = []
    for j in range(10):
        line = []
        for k in range(500):
            line.append(False)
        plane.append(line)
    grid.append(plane)

def place_bricks(bricks):
    for i in range(10):
        for j in range(10):
            for k in range(500):
                grid[i][j][k] = False
    for brick in bricks:
        start,end = brick
        for i in range(start[0],end[0]+1): 
            for j in range(start[1],end[1]+1): 
                for k in range(start[2],end[2]+1):
                    grid[i][j][k] = True
                    
place_bricks(bricks)

for x in range(100):
    for brick in bricks:
        empty = True
        start,end = brick
        while empty and start[2]>1:
            for i in range(start[0],end[0]+1): 
                    for j in range(start[1],end[1]+1):
                            if grid[i][j][start[2]-1]:
                                empty = False
            if empty and start[2]>1:
                for i in range(start[0],end[0]+1): 
                    for j in range(start[1],end[1]+1): 
                        grid[i][j][start[2]-1] = True
                        grid[i][j][end[2]] = False
                start[2] -= 1
                end[2] -= 1
                brick = (start,end)

total = 0
bricks_copy = bricks.copy()

for test_brick in bricks_copy:
    bricks.remove(test_brick)
    place_bricks(bricks)
    safe = True
    for brick in bricks:
        start,end = brick
        empty = True
        for i in range(start[0],end[0]+1): 
                for j in range(start[1],end[1]+1):
                        if grid[i][j][start[2]-1]:
                            empty = False
        if empty and start[2]>1:
            safe = False             
    if safe: total+=1
    bricks.append(test_brick)
print(total)
file = open("input.txt","r")
lines = file.read().split("\n")
# Part 1
bricks = []
for line in lines:
    start = [int(x) for x in line.split("~")[0].split(",")]
    end = [int(x) for x in line.split("~")[1].split(",")]
    bricks.append((start,end))
bricks.sort(key=lambda x: x[0][2])

grid = []
for i in range(10):
    plane = []
    for j in range(10):
        line = []
        for k in range(500):
            line.append(False)
        plane.append(line)
    grid.append(plane)

def place_brick(brick):
    start,end = brick
    for i in range(start[0],end[0]+1): 
        for j in range(start[1],end[1]+1): 
            for k in range(start[2],end[2]+1):
                grid[i][j][k] = True
                
def remove_brick(brick):
    start,end = brick
    for i in range(start[0],end[0]+1): 
        for j in range(start[1],end[1]+1): 
            for k in range(start[2],end[2]+1):
                grid[i][j][k] = False

def place_bricks(bricks):
    for i in range(10):
        for j in range(10):
            for k in range(500):
                grid[i][j][k] = False
    for brick in bricks:
        start,end = brick  
        empty = True      
        while empty and start[2]>1:
            for i in range(start[0],end[0]+1): 
                    for j in range(start[1],end[1]+1):
                            if grid[i][j][start[2]-1]:
                                empty = False
            if empty:
                start[2] -= 1
                end[2] -= 1
                brick = (start,end)
        place_brick(brick)    
                          
place_bricks(bricks)
                
for brick in bricks:
    empty = True
    start,end = brick
    while empty and start[2]>1:
        for i in range(start[0],end[0]+1): 
                for j in range(start[1],end[1]+1):
                        if grid[i][j][start[2]-1]:
                            empty = False
        if empty:
            for i in range(start[0],end[0]+1): 
                for j in range(start[1],end[1]+1): 
                    grid[i][j][start[2]-1] = True
                    grid[i][j][end[2]] = False
            start[2] -= 1
            end[2] -= 1
            brick = (start,end)

total = 0
for i in range(len(bricks)):
    remove_brick(bricks[i])
    safe = True
    for j in range(i+1,len(bricks)):
        start,end = bricks[j]
        empty = True
        for k in range(start[0],end[0]+1): 
                for l in range(start[1],end[1]+1):
                        if grid[k][l][start[2]-1]:
                            empty = False
        if empty and start[2]>1:
            safe = False
            break             
    if safe: total+=1
    place_brick(bricks[i])
print(total)
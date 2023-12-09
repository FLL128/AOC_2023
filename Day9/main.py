file = open("input.txt","r")
lines = file.read().split("\n")
# Part 1
total = 0
for line in lines:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    hist = [line]
    cur = line
    while set(cur) != {0}:
        new = []
        for i in range(len(cur)-1):
            new.append(cur[i+1]-cur[i])
        hist.append(new)
        cur = new
    cur = 0
    for i in range(len(hist)-1,-1,-1):
        cur += hist[i][-1]
    total += cur
print(total)

# Part 2
total = 0
for line in lines:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    hist = [line]
    cur = line
    while set(cur) != {0}:
        new = []
        for i in range(len(cur)-1):
            new.append(cur[i+1]-cur[i])
        hist.append(new)
        cur = new
    cur = 0
    for i in range(len(hist)-1,-1,-1):
        cur = hist[i][0]-cur
    total += cur
print(total)
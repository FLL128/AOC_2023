file = open("input.txt","r")
patterns = file.read().split("\n\n")

# Part 1
total = 0
for pattern in patterns:
    lines = pattern.split("\n")
    # Horizontal lines
    for i in range(1,len(lines)):
        works = True
        for j in range(1,min(len(lines)-i+1,i+1)):
            if lines[i-j]!=lines[i+j-1]:
                works = False
        if works:
            total += 100*(i)
    # Vertical lines
    for i in range(len(lines[0])):
        works = True
        for j in range(1,min(len(lines[0])-i+1,i+1)):
            for k in range(len(lines)):
                if lines[k][i-j]!=lines[k][i+j-1]:
                    works = False
        if works:
            total += (i)
print(total)

# Part 2
total = 0
for pattern in patterns:
    lines = pattern.split("\n")
    # Horizontal lines
    for i in range(1,len(lines)):
        cnt = 0
        for j in range(1,min(len(lines)-i+1,i+1)):
            for k in range(len(lines[0])):
                if lines[i-j][k]!=lines[i+j-1][k]:
                    cnt += 1
        if cnt == 1:
            total += 100*(i)
    # Vertical lines
    for i in range(len(lines[0])):
        cnt = 0
        for j in range(1,min(len(lines[0])-i+1,i+1)):
            for k in range(len(lines)):
                if lines[k][i-j]!=lines[k][i+j-1]:
                    cnt += 1
        if cnt == 1:
            total += (i)
print(total)
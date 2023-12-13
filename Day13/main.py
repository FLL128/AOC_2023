file = open("input.txt","r")
patterns = file.read().split("\n\n")

total1 = 0
total2 = 0
for pattern in patterns:
    lines = pattern.split("\n")
    # Horizontal lines
    for i in range(1,len(lines)):
        cnt = 0
        for j in range(1,min(len(lines)-i,i)+1):
            for k in range(len(lines[0])):
                if lines[i-j][k]!=lines[i+j-1][k]:
                    cnt += 1
        if cnt == 0:
            total1 += 100*i
        elif cnt == 1:
            total2 += 100*i
    # Vertical lines
    for i in range(len(lines[0])):
        cnt = 0
        for j in range(1,min(len(lines[0])-i,i)+1):
            for k in range(len(lines)):
                if lines[k][i-j]!=lines[k][i+j-1]:
                    cnt += 1
        if cnt == 0:
            total1 += i
        elif cnt == 1:
            total2 += i
print(total1)
print(total2)
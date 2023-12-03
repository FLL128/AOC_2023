file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
indic = []
for i in range(len(lines)):
    cur = []
    for j in range(len(lines[0])):
        cur.append(0)
    indic.append(cur)
for i, line in enumerate(lines):  
    for j, simb in enumerate(line):
        if simb not in "0123456789.":
            indic[i][j]=1
            if i>0: indic[i-1][j]=1
            if i>0 and j>0: indic[i-1][j-1]=1
            if i>0 and j<len(lines[0])-1: indic[i-1][j+1]=1
            if j>0: indic[i][j-1]=1
            if j<len(lines[0])-1: indic[i][j+1]=1
            if i<len(lines)-1: indic[i+1][j]=1
            if i<len(lines)-1 and j>0: indic[i+1][j-1]=1
            if i<len(lines)-1 and j<len(lines[0])-1: indic[i+1][j+1]=1

total = 0
cur = ""
inanum = False
picked = False
for i, line in enumerate(lines): 
    if inanum and picked: total += int(cur)
    cur = ""
    inanum = False
    picked = False
    for j, simb in enumerate(line):
        if simb in "0123456789":
            inanum = True
            cur += simb
            if indic[i][j]==1: picked = True
        elif inanum:
            inanum = False
            if picked: total += int(cur)
            picked = False
            cur=""
print(total)

# Part 2
def findnum(x,y):
    while(y>0 and lines[x][y-1] in "0123456789"): y -= 1
    cur=""
    while(y<len(lines[0]) and lines[x][y] in "0123456789"):
        cur += lines[x][y]
        y+=1
    return int(cur)
        
total = 0
for i, line in enumerate(lines):  
    for j, simb in enumerate(line):
        if simb == "*":
            neighbours = 0
            cur = 1
            for x in range(-1+(i==0),2-(i==len(lines)-1)):
                inanum = False
                for y in range(-1+(j==0),2-(j==len(lines[0])-1)):
                    if lines[i+x][j+y] in "0123456789" and not inanum:
                        inanum = True
                        neighbours += 1
                        cur *= findnum(i+x,j+y)
                    elif inanum and lines[i+x][j+y] not in "0123456789":
                        inanum = False
            if neighbours == 2:
                total += cur
print(total)
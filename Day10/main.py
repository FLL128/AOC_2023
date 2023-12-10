file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
found=False
loop = []
coords = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]=="S":
            coords.append([i,j])
            d=""
            if i>0 and lines[i-1][j] in "F7|":
                i=i-1
                d="u"
            elif j>0 and lines[i][j-1] in "F-L":
                j=j-1
                d="l"
            elif i<len(lines)-1 and lines[i+1][j] in "J|L":
                i=i+1
                d="d"
            else:
                j=j+1
                d="r"
            while lines[i][j] != "S":
                coords.append([i,j])
                loop.append(lines[i][j])
                if d=="u":
                    if lines[i][j]=="F":
                        j=j+1
                        d="r"
                    elif lines[i][j]=="7":
                        j=j-1
                        d="l"
                    else:
                        i=i-1
                elif d=="d":
                    if lines[i][j]=="L":
                        j=j+1
                        d="r"
                    elif lines[i][j]=="J":
                        j=j-1
                        d="l"
                    else:
                        i=i+1
                elif d=="r":
                    if lines[i][j]=="J":
                        i=i-1
                        d="u"
                    elif lines[i][j]=="7":
                        i=i+1
                        d="d"
                    else:
                        j=j+1
                else:
                    if lines[i][j]=="F":
                        i=i+1
                        d="d"
                    elif lines[i][j]=="L":
                        i=i-1
                        d="u"
                    else:
                        j=j-1
            print(int((len(loop)+1)/2))
            found = True
            break
    if found: break
    
# Part 2
newlines = []
for i in range(len(lines)):
    sub1 = ""
    sub2 = ""
    sub3 = ""
    for j in range(len(lines[0])):
        if [i,j] in coords:
            if lines[i][j] == "|":
                sub1+=" X "
                sub2+=" X "
                sub3+=" X "
            elif lines[i][j] == "-":
                sub1+="   "
                sub2+="XXX"
                sub3+="   "
            elif lines[i][j] == "L":
                sub1+=" X "
                sub2+=" XX"
                sub3+="   "
            elif lines[i][j] == "J":
                sub1+=" X "
                sub2+="XX "
                sub3+="   "
            elif lines[i][j] == "7":
                sub1+="   "
                sub2+="XX "
                sub3+=" X "
            elif lines[i][j] == "F":
                sub1+="   "
                sub2+=" XX"
                sub3+=" X "
            else:
                sub1+="XXX"
                sub2+="XXX"
                sub3+="XXX"
        else:
            sub1+="   "
            sub2+="   "
            sub3+="   "
    newlines.append(list(sub1))
    newlines.append(list(sub2))
    newlines.append(list(sub3))

'''
# Non recursive version - this would require S to be replaced with the correct letter, not just stars.
total = 0
for i in range(len(newlines)):
    j=0
    pr = False
    while j<len(newlines[0]):
        if newlines[i][j]=="X":
            a=newlines[i-1][j]+newlines[i+1][j]
            while newlines[i][j]=="X": j+=1
            b=newlines[i-1][j-1]+newlines[i+1][j-1]
            if a[0]=="X"==b[1] or a[1]=="X"==b[0]:
                pr = not pr
            j=j-1
        elif pr and i%3==1 and j%3==1:
            total += 1
            newlines[i][j]="I"
        j+=1
print(total)
'''

# Recursive (first) solution
def rec(x,y,d):
    if d>90: 
        rest.append([x,y])
        return
    newlines[x][y] = "O"
    if x>0 and newlines[x-1][y] not in "XO": rec(x-1,y,d+1)
    if y>0 and newlines[x][y-1] not in "XO": rec(x,y-1,d+1)
    if x<len(newlines)-1 and newlines[x+1][y] not in "XO": rec(x+1,y,d+1)
    if y<len(newlines[0])-1 and newlines[x][y+1] not in "XO": rec(x,y+1,d+1)
    return

rest = []
rec(0,0,0)
while rest != []:
    rest_copy = rest.copy()
    rest = []
    for i in rest_copy:
        rec(i[0],i[1],0)

total = 0
for i in range(1,len(newlines),3):
    for j in range(1,len(newlines[0]),3):
        if newlines[i][j] not in "XO": total+=1
print(total)
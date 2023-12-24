file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
def isFive(cards):
    if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]: return True
    return False

def isFour(cards):
    c_copy = sorted(cards)
    if c_copy[0] == c_copy[1] == c_copy[2] == c_copy[3]: return True
    if c_copy[1] == c_copy[2] == c_copy[3] == c_copy[4]: return True
    return False

def fullHouse(cards):
    a=[cards[0],0]
    b=""
    for i in cards:
        if a[0]==i: a[1]+=1
        elif b=="": b=[i,1]
        elif i==b[0]: b[1]+=1
    return (a[1]==2 and b[1]==3) or (b[1]==2 and a[1]==3)

def isThree(cards):
    a=[cards[0],0]
    b=[cards[1],0]
    c=[cards[2],0]
    for i in cards:
        if i==a[0]: a[1]+=1
        elif i==b[0]: b[1]+=1
        elif i==c[0]: c[1]+=1
    return a[1]==3 or b[1]==3 or c[1]==3

def twoPair(cards):
    c_copy = sorted(cards)
    if c_copy[0]==c_copy[1] and c_copy[2]==c_copy[3]: return True
    if c_copy[0]==c_copy[1] and c_copy[3]==c_copy[4]: return True
    if c_copy[1]==c_copy[2] and c_copy[3]==c_copy[4]: return True
    return False

def onePair(cards):
    c_copy = sorted(cards)
    return c_copy[0]==c_copy[1] or c_copy[1]==c_copy[2] or c_copy[2]==c_copy[3] or c_copy[3]==c_copy[4]

total = 0
for i in range(len(lines)):
    lines[i] = lines[i].split()
    line = lines[i]
    if isFive(line[0]): lines[i].append(7)
    elif isFour(line[0]): lines[i].append(6)
    elif fullHouse(line[0]): lines[i].append(5)
    elif isThree(line[0]): lines[i].append(4)
    elif twoPair(line[0]): lines[i].append(3)
    elif onePair(line[0]): lines[i].append(2)
    else: lines[i].append(1)

for line in lines:
    line[0]=line[0].replace("T","B").replace("J","C").replace("Q","D").replace("A","Z")
lines.sort(key = lambda x: (x[2], x[0]))
for i, line in enumerate(lines):
    total += int(line[1])*(i+1)
print(total)
    
# Part 2
total = 0
for i, line in enumerate(lines) :
    highest = 0
    for j in "23456789BDKZ":
        x = 0
        if isFive(line[0].replace("C",j)): x=7
        elif isFour(line[0].replace("C",j)): x=6
        elif fullHouse(line[0].replace("C",j)): x=5
        elif isThree(line[0].replace("C",j)): x=4
        elif twoPair(line[0].replace("C",j)): x=3
        elif onePair(line[0].replace("C",j)): x=2
        else: x=1
        highest = max(highest,x)
    lines[i][2] = highest

for line in lines:
    line[0]=line[0].replace("C","1")
lines.sort(key = lambda x: (x[2], x[0]))
for i, line in enumerate(lines):
    total += int(line[1])*(i+1)
print(total)
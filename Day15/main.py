file = open("input.txt","r")
line = file.read().split(",")

# Part 1
total = 0
for i in line:
    cur = 0
    for e in i:
        cur += ord(e)
        cur = cur * 17
        cur = cur % 256
    total += cur
print(total)

# Part 2
hashmap = [[] for i in range(256)]
for i in line:
    cur = 0
    label = i.split("=")[0].split("-")[0]
    for e in label:
        cur += ord(e)
        cur = cur * 17
        cur = cur % 256
    if "=" in i:
        notin = True
        for e in hashmap[cur]:
            if e[0]==label:
                e[1] = i.split("=")[1]
                notin = False
        if notin:
            hashmap[cur].append([label,i.split("=")[1]])
    else:
        for e in hashmap[cur]:
            if e[0]==label:
                hashmap[cur].remove(e)
                
total = 0
for i in range(256):
    for j in range(len(hashmap[i])):
        total += (int(hashmap[i][j][1]))*(j+1)*(i+1)
print(total)
            
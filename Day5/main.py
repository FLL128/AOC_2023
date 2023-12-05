file = open("input.txt","r")
maps = file.read().split("\n\n")

# Part 1
numbers = maps[0].split(":")[1].split()
for cur_m in maps[1:]:
    newnumbers = []
    ranges = cur_m.split(":")[1].split("\n")[1:]
    for number in numbers:
        found = False
        for curr in ranges:
            curr = curr.split()
            if int(number) >= int(curr[1]) and int(number) < int(curr[1])+int(curr[2]):
                newnumbers.append(int(curr[0])+int(number)-int(curr[1]))
                found = True
        if not found: newnumbers.append(number)
    numbers = newnumbers
numbers.sort()
print(numbers[0])

# Part 2
numberlist = maps[0].split(":")[1].split()
numbers = []
seed = True
cur = []
for i in numberlist:
    cur.append(int(i))
    if seed:
        seed = False
    else:
        seed = True
        numbers.append(cur)
        cur = []
for cur_m in maps[1:]:
    newnumbers = []
    ranges = cur_m.split(":")[1].split("\n")[1:]
    for i in range(len(ranges)):
        ranges[i] = ranges[i].split()
    ranges.sort(key = lambda x: x[1])
    for number in numbers:
        found = False
        for curr in ranges:
            start = int(curr[1])
            length = int(curr[2])
            dest = int(curr[0])
            if number[0] < start+length and number[0]+number[1] > start:
                if number[0] <= start:
                    if number[0] != start: newnumbers.append([number[0],start-number[0]])
                    number[1] = number[1]-start+number[0]
                    number[0] = start
                    if number[1] <= length:
                        newnumbers.append([dest,number[1]])
                        found = True
                    else:
                        newnumbers.append([dest,length])
                        number[0] += length
                        number[1] -= length
                else:
                    if number[0]+number[1] <= start+length:
                        newnumbers.append([dest+number[0]-start,number[1]])
                        found = True
                    else:
                        newnumbers.append([dest+number[0]-start,length+start-number[0]])
                        number[1] -= (length+start-number[0])
                        number[0] = start+length
        if not found: newnumbers.append(number)
    numbers = newnumbers
numbers.sort()
print(numbers[0][0])
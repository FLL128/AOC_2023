import math
file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
times = lines[0].split(":")[1:][0].split()
distances = lines[1].split(":")[1:][0].split()
total = 1
for i in range(len(times)):
    cur = 0
    for j in range(int(times[i])):
        if int(distances[i]) < j*(int(times[i])-j) : cur+=1
    total *= cur
print(total)

# Part 2
time = int(lines[0].split(":")[1:][0].replace(" ",""))
distance = int(lines[1].split(":")[1:][0].replace(" ",""))
for i in range(0,time,int(math.sqrt(time))):
    if (time-i)*i > distance:
        for j in range(i-int(math.sqrt(time)),i+1,1):
            if (time-j)*j > distance:
                print(time-j*2+1)
                break
        break
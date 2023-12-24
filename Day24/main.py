file = open("input.txt","r")
lines = file.read().split("\n")
# Part 1
locations = []
speeds = []
for line in lines:
    locations.append([int(x) for x in line.split("@")[0].strip().split(", ")])
    speeds.append([int(x) for x in line.split("@")[1].strip().split(", ")])

total = 0
for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        x1 = locations[i][0]
        y1 = locations[i][1]
        x2 = x1 + speeds[i][0]
        y2 = y1 + speeds[i][1]
        x3 = locations[j][0]
        y3 = locations[j][1]
        x4 = x3 + speeds[j][0]
        y4 = y3 + speeds[j][1]
        if (x1-x2)*(y3-y4) != (y1-y2)*(x3-x4):
            Px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
            Py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
            mi = 200000000000000
            ma = 400000000000000
            if mi <= Px <= ma and mi <= Py <= ma:
                if ((x1 < Px and x2 > x1) or (x1 > Px and x2 < x1)) and \
                    ((x3 < Px and x4 > x3) or (x3 > Px and x4 < x3)) and \
                    ((y1 < Py and y2 > y1) or (y1 > Py and y2 < y1)) and \
                    ((y3 < Py and y4 > y3) or (y3 > Py and y4 < y3)):
                    total += 1
print(total)

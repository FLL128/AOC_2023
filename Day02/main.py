file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
total = 0
for line in lines:
    game = line.split(":")[1]
    pulls = game.split(";")
    possible = True
    for pull in pulls:
        sets = pull.split(",")
        for oneset in sets:
            count = oneset.split()[0]
            colour = oneset.split()[1]
            if colour == "red" and int(count)>12: possible = False
            elif colour == "green" and int(count)>13: possible = False
            elif colour == "blue" and int(count)>14: possible = False
    if possible: total += int(line.split(":")[0][4:])
print(total)

# Part 2
total = 0
for line in lines:
    game = line.split(":")[1]
    pulls = game.split(";")
    reds = 0
    greens = 0
    blues = 0
    for pull in pulls:
        sets = pull.split(",")
        for oneset in sets:
            count = oneset.split()[0]
            colour = oneset.split()[1]
            if colour == "red" and int(count)>reds: reds = int(count)
            elif colour == "green" and int(count)>greens: greens = int(count)
            elif colour == "blue" and int(count)>blues: blues = int(count)
    total += reds*greens*blues
print(total)
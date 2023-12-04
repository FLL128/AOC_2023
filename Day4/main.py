file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
total = 0
for line in lines:
    number = line.split(":")[0]
    cards = line.split(":")[1].strip()
    winners = cards.split("|")[0].split()
    mine = cards.split("|")[1].split()
    cardvalue = 0.5
    for i in mine:
        if i in winners:
            cardvalue *= 2
    if cardvalue == 0.5: cardvalue = 0
    total += int(cardvalue)
print(total)
    
# Part 2
total = 0
counter = []
for i in range(len(lines)):
    counter.append(1)
for i, line in enumerate(lines):
    number = line.split(":")[0]
    cards = line.split(":")[1].strip()
    winners = cards.split("|")[0].split()
    mine = cards.split("|")[1].split()
    total += counter[i]
    cur = 1
    for num in mine:
        if num in winners:
            counter[i+cur]+=counter[i]
            cur+=1
print(total)
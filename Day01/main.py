file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
total = 0
for line in lines:
    digits = ""
    for char in line:
        if char in "0123456789":
            digits += char
    number = digits[0]+digits[-1]
    total += int(number)
print(total)

# Part 2
total = 0
for line in lines:
    line = line.replace("one","one1one").replace("two","two2two").replace("three","three3three")
    line = line.replace("four","four4four").replace("five","five5five").replace("six","six6six")
    line = line.replace("seven","seven7seven").replace("eight","eight8eight").replace("nine","nine9nine")
    digits = ""
    for char in line:
        if char in "0123456789":
            digits += char
    number = digits[0]+digits[-1]
    total += int(number)
print(total)
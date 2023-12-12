import functools

file = open("input.txt","r")
lines = file.read().split("\n")

# Part 1
def rec(springs,numbers,index):
    total = 0
    if index==len(springs):
        numbers_copy = numbers.copy()
        i = 0
        damaged = False
        for e in springs:
            if i>=len(numbers_copy) and e=="#":
                return 0
            if e=="#" and not damaged:
                damaged = True
                numbers_copy[i]-=1
            elif e=="#":
                if numbers_copy[i]<=0:
                    return 0
                else: numbers_copy[i]-=1
            elif damaged: 
                if numbers_copy[i]!=0:
                    return 0
                damaged = False
                i+=1
        if damaged:
            if numbers_copy[i]!=0:
                return 0
            i+=1
        if i<len(numbers_copy): return 0
        return 1
    if springs[index]=="?":
        springs[index] = "#"
        total += rec(springs,numbers,index+1)
        springs[index] = "."
        total += rec(springs,numbers,index+1)
        springs[index] = "?"
        return total
    else:
        return rec(springs,numbers,index+1)

total=0
for line in lines:
    springs = list(line.split()[0])
    numbers = list(line.split()[1].split(","))
    for i in range(len(numbers)):
        numbers[i]=int(numbers[i])
    cur = rec(springs,numbers,0)
    total += cur
print(total)

# Part 2
@functools.cache
def rec2(springs,numbers,i,c,damaged):
    if len(springs)==0:
        if damaged:
            if numbers[i]!=c:
                return 0
            i+=1
        if i<len(numbers):
            return 0
        return 1
    elif springs[0]=="?":
        new_springs = "#"+springs[1:]
        total = rec2(new_springs,numbers,i,c,damaged)
        new_springs = "."+springs[1:]
        total += rec2(new_springs,numbers,i,c,damaged)
        return total
    elif i>=len(numbers) and springs[0]=="#":
        return 0
    elif springs[0]=="#" and not damaged:
        return rec2(springs[1:],numbers,i,c+1,True)
    elif springs[0]=="#":
        if numbers[i]<c:
            return 0
        else: 
            return rec2(springs[1:],numbers,i,c+1,damaged)
    elif damaged:
        if numbers[i]!=c:
            return 0
        return rec2(springs[1:],numbers,i+1,0,False)
    return rec2(springs[1:],numbers,i,c,damaged)
   
total=0
for line in lines:
    springs = line.split()[0]
    numbers = list(line.split()[1].split(","))
    springs = springs+'?'+springs+'?'+springs+'?'+springs+'?'+springs
    numbers = numbers+numbers+numbers+numbers+numbers
    for i in range(len(numbers)):
        numbers[i]=int(numbers[i])
    numbers = tuple(numbers)
    cur = rec2(springs,numbers,0,0,False)
    total += cur
print(total)
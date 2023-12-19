file = open("input.txt","r")
parts = file.read().split("\n\n")
workflows = parts[0].split("\n")
ratings = parts[1].split("\n") 
names = {}
rules = []
parts = []

# Part 1
for i in range(len(workflows)):
    line = workflows[i].split("{")
    name = line[0]
    rule = line[1][:-1].split(",")
    names[name] = i
    rules.append(rule)
for i in range(len(ratings)):
    parts.append(ratings[i][1:-1])

def rec(rule,part):
    new_workshop = ""
    for r in rule:
        if r[0]=="x":
            if r[1]=="<" and int(part.split(",")[0][2:]) < int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
            if r[1]==">" and int(part.split(",")[0][2:]) > int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
        if r[0]=="m":
            if r[1]=="<" and int(part.split(",")[1][2:]) < int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
            if r[1]==">" and int(part.split(",")[1][2:]) > int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
        if r[0]=="a":
            if r[1]=="<" and int(part.split(",")[2][2:]) < int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
            if r[1]==">" and int(part.split(",")[2][2:]) > int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
        if r[0]=="s":
            if r[1]=="<" and int(part.split(",")[3][2:]) < int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
            if r[1]==">" and int(part.split(",")[3][2:]) > int(r.split(":")[0][2:]):
                new_workshop = r.split(":")[1]
                break
        if r=="A": return 1
        if r=="R": return 0
        if new_workshop=="" and ":" not in r: new_workshop = r
    if new_workshop=="A": return 1
    if new_workshop=="R": return 0
    return rec(rules[names[new_workshop]],part)

total = 0
for part in parts:
    value = int(part.split(",")[0][2:])+int(part.split(",")[1][2:])+int(part.split(",")[2][2:])+int(part.split(",")[3][2:])
    total += rec(rules[names["in"]],part)*value
print(total)

# Part 2
def rec2(rule,x_min,x_max,m_min,m_max,a_min,a_max,s_min,s_max):
    total = 0
    for r in rule:
        if r[0]=="x":
            if r[1]=="<" and x_min < int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,int(r.split(":")[0][2:])-1,m_min,m_max,a_min,a_max,s_min,s_max)
                x_min = int(r.split(":")[0][2:])
                continue
            if r[1]==">" and x_max > int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],int(r.split(":")[0][2:])+1,x_max,m_min,m_max,a_min,a_max,s_min,s_max)
                x_max = int(r.split(":")[0][2:])
                continue
        if r[0]=="m":
            if r[1]=="<" and m_min < int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,x_max,m_min,int(r.split(":")[0][2:])-1,a_min,a_max,s_min,s_max)
                m_min = int(r.split(":")[0][2:])
                continue
            if r[1]==">" and m_max > int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,x_max,int(r.split(":")[0][2:])+1,m_max,a_min,a_max,s_min,s_max)
                m_max = int(r.split(":")[0][2:])
                continue
        if r[0]=="a":
            if r[1]=="<" and a_min < int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,x_max,m_min,m_max,a_min,int(r.split(":")[0][2:])-1,s_min,s_max)
                a_min = int(r.split(":")[0][2:])
                continue
            if r[1]==">" and a_max > int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,x_max,m_min,m_max,int(r.split(":")[0][2:])+1,a_max,s_min,s_max)
                a_max = int(r.split(":")[0][2:])
                continue
        if r[0]=="s":
            if r[1]=="<" and s_min < int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,x_max,m_min,m_max,a_min,a_max,s_min,int(r.split(":")[0][2:])-1)
                s_min = int(r.split(":")[0][2:])
                continue
            if r[1]==">" and s_max > int(r.split(":")[0][2:]):
                total += rec2(rules[names[r.split(":")[1]]],x_min,x_max,m_min,m_max,a_min,a_max,int(r.split(":")[0][2:])+1,s_max)
                s_max = int(r.split(":")[0][2:])
                continue
        if ":" not in r:
            if r=="A": return total + (x_max-x_min+1)*(m_max-m_min+1)*(a_max-a_min+1)*(s_max-s_min+1)
            if r=="R": return total
            return total + rec2(rules[names[r]],x_min,x_max,m_min,m_max,a_min,a_max,s_min,s_max)

rules.append("A")
rules.append("R")
names["A"] = len(workflows)
names["R"] = len(workflows)+1
print(rec2(rules[names["in"]],1,4000,1,4000,1,4000,1,4000))
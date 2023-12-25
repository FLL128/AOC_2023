file = open("input.txt","r")
modules = file.read().split("\n")

# Part 1
start = []
mapping = {}
for module in modules:
    module = module.split("->")
    name = module[0].strip()
    receps = module[1].strip().split(", ")
    if name!="broadcaster":
        m_type = name[0]
        name = name[1:]
        mapping[name] = [m_type,False,{},receps]
    else:
        for recep in receps:
            start.append((recep,"l","broadcaster"))
        
new_map = mapping.copy()
for e in new_map:
    for recep in mapping[e][3]:
        if recep not in mapping:
            mapping[recep] = [".",False,[],[]]
        
for e in mapping:
    for recep in mapping[e][3]:
        if mapping[recep][0]=="&":
            mapping[recep][2][e]="l"

# Mapping[type,state,inputdict,outputlist]
countl = 0
counth = 0
for i in range(1000):
    countl += 1
    signals = start.copy()
    while signals!=[]:
        cur = signals.pop(0)
        if mapping[cur[0]][0]=="&":
            mapping[cur[0]][2][cur[2]]=cur[1]
            output = "l"
            for sender in mapping[cur[0]][2]:
                if mapping[cur[0]][2][sender] == "l":
                    output = "h"
            for recep in mapping[cur[0]][3]:
                signals.append((recep,output,cur[0]))
        elif mapping[cur[0]][0]=="%":
            if cur[1]=="l":
                mapping[cur[0]][1] = not mapping[cur[0]][1]
                output = "lh"[mapping[cur[0]][1]]
                for recep in mapping[cur[0]][3]:
                    signals.append((recep,output,cur[0]))
        if cur[1]=="l": countl+=1
        else: counth+=1
print(countl*counth)


# Part 2
def count_until_high(name):
    count = 1
    while True:
        signals = start.copy()
        while signals!=[]:
            cur = signals.pop(0)
            if mapping[cur[0]][0]=="&":
                mapping[cur[0]][2][cur[2]]=cur[1]
                output = "l"
                for sender in mapping[cur[0]][2]:
                    if mapping[cur[0]][2][sender] == "l":
                        output = "h"
                for recep in mapping[cur[0]][3]:
                    signals.append((recep,output,cur[0]))
                    if output == "h" and name==cur[0]: return count
            elif mapping[cur[0]][0]=="%":
                if cur[1]=="l":
                    mapping[cur[0]][1] = not mapping[cur[0]][1]
                    output = "lh"[mapping[cur[0]][1]]
                    for recep in mapping[cur[0]][3]:
                        signals.append((recep,output,cur[0]))
        count += 1

final_sender = ""
for name in mapping:
    if mapping[name][3] == ["rx"]:
        final_sender = name
final_set_high = []
for name in mapping:
    if final_sender in mapping[name][3]: final_set_high.append(name)

total = 1  
for n in final_set_high:
    start = []
    mapping = {}
    for module in modules:
        module = module.split("->")
        name = module[0].strip()
        receps = module[1].strip().split(", ")
        if name!="broadcaster":
            m_type = name[0]
            name = name[1:]
            mapping[name] = [m_type,False,{},receps]
        else:
            for recep in receps:
                start.append((recep,"l","broadcaster"))
    new_map = mapping.copy()
    for e in new_map:
        for recep in mapping[e][3]:
            if recep not in mapping:
                mapping[recep] = [".",False,[],[]]
    for e in mapping:
        for recep in mapping[e][3]:
            if mapping[recep][0]=="&":
                mapping[recep][2][e]="l"

    total *= count_until_high(n)
print(total)
import re

def couldBeFirst(sequence:list, index:int, Dictionary:dict):
    out = 1
    element = sequence[index]
    for s in sequence:
        if not s == element and s in Dictionary[element]:
            out = 0
            break
    return out

if __name__ == '__main__':
    with open('Input05.txt') as f:
        arrayRaw = f.readlines()
     
maxDict = {}
maxkeys = []
minDict = {}
minkeys = []   

for line in arrayRaw:
    num = line.replace('\n','').split('|')
    if num[0] in minkeys:
        minDict[num[0]].append(num[1])
    else:
        minDict.update({num[0]: [num[1]]})
        minkeys.append(num[0])
    if num[1] in maxkeys:
        maxDict[num[1]].append(num[0])
    else:
        maxDict.update({num[1]: [num[0]]})
        maxkeys.append(num[1])

with open('Input05_02.txt') as f:
    totList = f.readlines()
    
# First star
tot = 0 
disorderList = []      
for order in totList:
    order = order.replace('\n','').split(',')
    correct = 1
    i = 0
    while i<len(order) and correct:
        if order[i] in minkeys:
            if any([order[j] in minDict[order[i]] for j in range(i)]):
                correct = 0
                disorderList.append(order)
        if correct and order[i] in maxkeys:
            if any([order[j] in maxDict[order[j]] for j in range(i+1,len(order))]):
                correct = 0
                disorderList.append(order)

        i += 1
    if correct:
        tot += float(order[round((len(order)-1)/2)])

print(tot)
              
         
# Second star
tot = 0
for l in disorderList:
    orderlist = []
    for i in range(round((len(l)+1)/2)):
        j=0
        found = 0
        while j<len(l) and not found:
            if couldBeFirst(l,j,maxDict):
                found = 1
                orderlist.append(l[j])
                l.pop(j)
            else:
                j += 1
    tot += float(orderlist[-1])
print(tot)

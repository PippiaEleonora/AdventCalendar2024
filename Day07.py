import math

def selectOperator(list,result,secondStar):
    n = math.floor(math.log10(list[1]))+1
    if len(list)==2:
        if list[0]*list[1] == result:
            return 1
        elif list[0]+list[1] == result:
            return 1
        elif secondStar and list[0]*(10**n) + list[1] == result:
             return 1
        else:
            return 0
    else:
        mulList = [list[0]*list[1]] + list[2:]
        addList = [list[0]+list[1]] + list[2:]
        conList = [list[0]*(10**n)+list[1]] + list[2:]
        if selectOperator(mulList,result,secondStar):
            return 1
        elif selectOperator(addList,result,secondStar):
            return 1
        elif secondStar and selectOperator(conList, result,secondStar):
             return 1
        else:
            return 0
            
            
if __name__ == '__main__':
    with open('Input07.txt') as f:
        arrayRaw = f.readlines()
     
result =[]
numbers = []
for line in arrayRaw:
    values = line.replace('\n','').split(': ')
    result.append(float(values[0]))
    numbersString = values[1].split(' ')
    numbers.append([float(n) for n in numbersString])

# First Star
tot = 0
for i in range(len(numbers)):
    list = numbers[i]
    mulList = [list[0]*list[1]] + list[2:]
    addList = [list[0]+list[1]] + list[2:]
    if selectOperator(mulList,result[i],0):
        tot += result[i]
    elif selectOperator(addList,result[i],0):
        tot += result[i]
        
print(tot)

# Second Star
tot = 0
for i in range(len(numbers)):
    list = numbers[i]
    n = math.floor(math.log10(list[1]))+1
    mulList = [list[0]*list[1]] + list[2:]
    addList = [list[0]+list[1]] + list[2:]
    conList = [list[0]*(10**n)+list[1]] + list[2:]
    if selectOperator(mulList,result[i],1):
        tot += result[i]
    elif selectOperator(addList,result[i],1):
        tot += result[i]
    elif selectOperator(conList, result[i],1):
        tot += result[i]
        
print(tot)

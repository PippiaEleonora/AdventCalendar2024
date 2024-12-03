import re

def countMul(string:str) -> int:
    match = re.findall('mul\([0-9]+,[0-9]+\)',string)
    numString = [re.findall('[0-9]+',x)for x in match]
    tot = 0
    for n in numString:
        tot += float(n[0])*float(n[1])
    return tot

if __name__ == '__main__':
    with open('Input03.txt') as f:
        arrayRaw = f.readlines()
        
arrayRaw = '\n'.join(arrayRaw)

#First star
tot = countMul(arrayRaw)
print(tot)

#Second star
splitting1 = arrayRaw.split("don't()")
splitting2 = [x.split('do()') for x in splitting1]
splittingCollection = [splitting1[0]] + ['\n'.join(x[1:]) for x in splitting2 if len(x)>1]
RawString = '\n'.join(splittingCollection)
tot = countMul(RawString)
print(tot)

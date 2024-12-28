from tqdm import tqdm

def findPattern_AI(pattern, Towels, found):
    if pattern in found:
        return found[pattern]
    if pattern == "":
        return 1
    result = 0
    for towel in Towels:
        if pattern.startswith(towel):
            result += findPattern_AI(pattern[len(towel):], Towels, found)
    found[pattern] = result
    return result

def findPattern(pattern, Towels, bound, found):
    result = 0
    for d in range(bound[0],bound[1]+1):
        if d<len(pattern):
            if pattern[:d] in Towels:
                if pattern[d:] in list(found.keys()):
                    result += found[pattern[d:]]
                    found[pattern] = found.get(pattern, 0) + found[pattern[d:]]
                else:
                    result += findPattern(pattern[d:], Towels, bound, found)
                    found[pattern] = result
        elif d == len(pattern):
            if pattern in Towels:
                found[pattern] = found.get(pattern, 0) + 1
                return result + 1
            else:
                return result
        else:
            return result
    return result

if __name__ == '__main__':
    with open('Input19.txt') as f:
        arrayRaw = f.readlines()

Towels = arrayRaw[0].replace('\n','').split(', ')

Dim = [len(t) for t in Towels]
minD = min(Dim)
maxD = max(Dim)

FirstStar = 0
SecondStar = 0
for i in tqdm(range(2,len(arrayRaw))):
    pattern = arrayRaw[i].replace('\n','')
    result = findPattern(pattern, Towels, [minD,maxD], {})
    if result>0:
        FirstStar +=1
        SecondStar += result
print(FirstStar)
print(SecondStar)

FirstStar = 0
SecondStar = 0
for i in tqdm(range(2,len(arrayRaw))):
    pattern = arrayRaw[i].replace('\n','')
    result = findPattern_AI(pattern, Towels, {})
    if result>0:
        FirstStar +=1
        SecondStar += result
print(FirstStar)
print(SecondStar)


#1041529704688380

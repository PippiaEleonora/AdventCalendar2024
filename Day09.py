
if __name__ == '__main__':
    with open('Input09.txt') as f:
        arrayRaw = f.readlines()
        
line = arrayRaw[0].replace('\n','')
line = [int(l) for l in line]
n = len(line)

# First Star
if n%2:
    last = int(n-1)
else:
    last = int(n-2)
lastId = last/2
curr = 1
currId = 1
FinalList = [[0,line[0]]]
tot = 0
while curr<last:
    space = line[curr]
    last_dimension = line[last]
    if space>0:
        if last_dimension>space:
            line[last] -= space
            for j in range(space):
                tot += lastId*(sum(line[0:curr])+j)
            for j in range(line[curr+1]):
                tot += currId*(sum(line[0:curr+1])+j)
            curr += 2
            currId += 1
        elif last_dimension==space:
            line[last] -= space
            for j in range(space):
                tot += lastId*(sum(line[0:curr])+j)
            for j in range(line[curr+1]):
                tot += currId*(sum(line[0:curr+1])+j)
            curr += 2
            currId += 1
            last -= 2
            lastId -= 1
        else:
            for j in range(line[last]):
                tot += lastId*(sum(line[0:curr])+j)
            line[curr] -= line[last]
            line[curr-1] += line[last]
            line[last] = 0
            last -= 2
            lastId -= 1
    else:
        for j in range(line[curr+1]):
                tot += currId*(sum(line[0:curr+1])+j)
        curr += 2
        currId += 1
        
print(tot)


# Second Star
line = arrayRaw[0].replace('\n','')
line = [int(l) for l in line]
if n%2:
    last = int(n-1)
else:
    last = int(n-2)
lastId = last/2
curr = 1
currId = 1
FinalList = [[0,line[0]]]
tot = 0
lineSpace = line.copy()
while 1<last:
    # print([last, lastId,  line[last]])
    curr = 1
    placed = 0
    while curr<last and not placed:
        space = lineSpace[curr]
        last_dimension = line[last]
        if space>0:
            if last_dimension>space:
                curr += 2
            elif last_dimension==space:
                lineSpace[last] -= space
                for j in range(space):
                    tot += lastId*(sum(lineSpace[0:curr])+j)
                lineSpace[curr-1] += space
                lineSpace[curr] = 0
                placed = 1
                last -= 2
                lastId -= 1
            else:
                for j in range(last_dimension):
                    tot += lastId*(sum(lineSpace[0:curr])+j)
                placed = 1
                lineSpace[curr-1] += last_dimension
                lineSpace[curr] -= last_dimension
                lineSpace[last] = 0
                last -= 2
                lastId -= 1
                
        else:
            curr += 2
    if not placed:
        for j in range(last_dimension):
            tot += lastId*(sum(lineSpace[0:last])+j)
        last -= 2
        lastId -= 1
        
print(tot)
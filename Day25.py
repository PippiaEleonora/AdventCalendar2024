if __name__ == '__main__':
    with open('Input25.txt') as f:
        arrayRaw = f.readlines()

Key = []
currK = -1
Lock = []
currL = -1

i = 0

while i<len(arrayRaw):
    line_start = arrayRaw[i].replace('\n','')
    if line_start == '#####':
        Key.append([0,0,0,0,0])
        currK +=1
        for j in range(5):
            for k in range(5):
                if arrayRaw[i+j+1][k] == '#':
                    Key[currK][k] += 1
        i = i + 5 + 3
    else:
        Lock.append([0, 0, 0, 0, 0])
        currL += 1
        for j in range(5):
            for k in range(5):
                if arrayRaw[i + j + 1][k] == '#':
                    Lock[currL][k] += 1
        i = i + 5 + 3

tot = 0
for L1 in Lock:
    for K1 in Key:
        if all([L1[i]+K1[i]<6 for i in range(5)]):
            tot += 1
print(tot)


if __name__ == '__main__':
    with open('Input15.txt') as f:
        arrayRaw = f.readlines()

ArrayMatrix = []
i = 0
line = arrayRaw[i].replace('\n', '')
while not line == '':
    if '@' in line:
        StartP = [i,line.index('@')]
    line = line.replace('@','.')
    for j in range(len(line)):
        if j == 0:
            ArrayMatrix.append([])
        ArrayMatrix[i].append(line[j])
    i += 1
    line = arrayRaw[i].replace('\n', '')

ArrayMatrix_flip = []
for j in range(len(ArrayMatrix[0])):
    for k in range(len(ArrayMatrix)):
        if k == 0:
            ArrayMatrix_flip.append([ArrayMatrix[k][j]])
        else:
            ArrayMatrix_flip[j] += ArrayMatrix[k][j]

Path = ''
for j in range(i+1,len(arrayRaw)):
    Path += arrayRaw[j].replace('\n', '')

dictionary = {'<':[0,-1], '>':[0,+1], '^':[-1,0], 'v':[+1,0]}
currP = StartP
for move in Path:
    nextP = [currP[0]+dictionary[move][0], currP[1]+dictionary[move][1]]
    if ArrayMatrix[nextP[0]][nextP[1]] == '.': #free move
        currP = nextP
    elif ArrayMatrix[nextP[0]][nextP[1]] == 'O': #block
        if move == '>' and '.' in ArrayMatrix[nextP[0]][nextP[1]:]:
            idempty = ArrayMatrix[nextP[0]][nextP[1]:].index('.')
            idblock = ArrayMatrix[nextP[0]][nextP[1]:].index('#')
            if idempty<idblock:
                ArrayMatrix[nextP[0]][nextP[1]] = '.'
                ArrayMatrix[nextP[0]][nextP[1]+idempty] = 'O'
                ArrayMatrix_flip[nextP[1]][nextP[0]] = '.'
                ArrayMatrix_flip[nextP[1]+idempty][nextP[0]] = 'O'
                currP = nextP
        elif move == '<' and '.' in ArrayMatrix[nextP[0]][:nextP[1]]:
            idempty = ArrayMatrix[nextP[0]][nextP[1]::-1].index('.')
            idblock = ArrayMatrix[nextP[0]][nextP[1]::-1].index('#')
            if idempty < idblock:
                ArrayMatrix[nextP[0]][nextP[1]] = '.'
                ArrayMatrix[nextP[0]][nextP[1]-idempty] = 'O'
                ArrayMatrix_flip[nextP[1]][nextP[0]] = '.'
                ArrayMatrix_flip[nextP[1]-idempty][nextP[0]] = 'O'
                currP = nextP
        elif move == '^' and '.' in ArrayMatrix_flip[nextP[1]][:nextP[0]]:
            idempty = ArrayMatrix_flip[nextP[1]][nextP[0]::-1].index('.')
            idblock = ArrayMatrix_flip[nextP[1]][nextP[0]::-1].index('#')
            if idempty < idblock:
                ArrayMatrix[nextP[0]][nextP[1]] = '.'
                ArrayMatrix[nextP[0]-idempty][nextP[1]] = 'O'
                ArrayMatrix_flip[nextP[1]][nextP[0]] = '.'
                ArrayMatrix_flip[nextP[1]][nextP[0]-idempty] = 'O'
                currP = nextP
        elif move == 'v' and '.' in ArrayMatrix_flip[nextP[1]][nextP[0]:]:
            idempty = ArrayMatrix_flip[nextP[1]][nextP[0]:].index('.')
            idblock = ArrayMatrix_flip[nextP[1]][nextP[0]:].index('#')
            if idempty < idblock:
                ArrayMatrix[nextP[0]][nextP[1]] = '.'
                ArrayMatrix[nextP[0]+idempty][nextP[1]] = 'O'
                ArrayMatrix_flip[nextP[1]][nextP[0]] = '.'
                ArrayMatrix_flip[nextP[1]][nextP[0]+idempty] = 'O'
                currP = nextP


tot = 0
for i in range(len(ArrayMatrix)):
    for j in range(len(ArrayMatrix[0])):
        if ArrayMatrix[i][j] == 'O':
            tot += 100*i+j
print(tot)
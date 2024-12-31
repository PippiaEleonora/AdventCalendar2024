import copy
def canMove(listbox,d,ArrayMatrix,ArrayMatrix_flip):
    listbox_new = []
    for box in listbox:
        b1 = box[0]
        b2 = box[1]
        if ArrayMatrix[b1[0]+d][b1[1]] == ']':
            box_new = [[b1[0]+d,b1[1]-1],[b1[0]+d,b1[1]]]
            listbox_new.append(box_new)
            ArrayMatrix[b1[0] + d][b1[1]] = '['
            ArrayMatrix_flip[b1[1]][b1[0] + d] = '['
            ArrayMatrix[b1[0] + d][b1[1]-1] = '.'
            ArrayMatrix_flip[b1[1]-1][b1[0] + d] = '.'
            if ArrayMatrix[b2[0] + d][b2[1]] == '[':
                box_new = [[b2[0] + d, b2[1]], [b2[0] + d, b2[1] + 1]]
                listbox_new.append(box_new)
                ArrayMatrix[b2[0] + d][b2[1]] = ']'
                ArrayMatrix_flip[b2[1]][b2[0] + d] = ']'
                ArrayMatrix[b2[0] + d][b2[1]+1] = '.'
                ArrayMatrix_flip[b2[1]+1][b2[0] + d] = '.'
            elif ArrayMatrix[b2[0] + d][b2[1]] == '.':
                ArrayMatrix[b2[0] + d][b2[1]] = ']'
                ArrayMatrix_flip[b2[1]][b2[0] + d] = ']'
            else:
                return 0, [], []
        elif ArrayMatrix[b1[0]+d][b1[1]] == '[':
            box_new = [[b1[0]+d,b1[1]],[b2[0]+d,b2[1]]]
            listbox_new.append(box_new)
        elif ArrayMatrix[b1[0]+d][b1[1]] == '.':
            ArrayMatrix[b1[0] + d][b1[1]] = '['
            ArrayMatrix_flip[b1[1]][b1[0] + d] = '['
            if ArrayMatrix[b2[0] + d][b2[1]] == '[':
                box_new = [[b2[0] + d, b2[1]], [b2[0] + d, b2[1]+1]]
                listbox_new.append(box_new)
                ArrayMatrix[b2[0] + d][b2[1]] = ']'
                ArrayMatrix_flip[b2[1]][b2[0] + d] = ']'
                ArrayMatrix[b2[0] + d][b2[1] + 1] = '.'
                ArrayMatrix_flip[b2[1] + 1][b2[0] + d] = '.'
            elif ArrayMatrix[b2[0] + d][b2[1]] == '.':
                ArrayMatrix[b2[0] + d][b2[1]] = ']'
                ArrayMatrix_flip[b2[1]][b2[0] + d] = ']'
            else:
                return 0, [], []
        else:
            return 0, [], []
    if len(listbox_new)>0:
        return canMove(listbox_new, d, ArrayMatrix, ArrayMatrix_flip)
    else:
        return 1, ArrayMatrix, ArrayMatrix_flip





if __name__ == '__main__':
    with open('Input15.txt') as f:
        arrayRaw = f.readlines()

ArrayMatrix = []
i = 0
line = arrayRaw[i].replace('\n', '')
while not line == '':
    if '@' in line:
        StartP = [i,2*line.index('@')]
    line = line.replace('@','.')
    for j in range(len(line)):
        if j == 0:
            ArrayMatrix.append([])
        if line[j] in ['.', '#']:
            ArrayMatrix[i] += [line[j], line[j]]
        else:
            ArrayMatrix[i] += ['[', ']']

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
    elif ArrayMatrix[nextP[0]][nextP[1]] in ['[',']']: #block
        if move == '>' and '.' in ArrayMatrix[nextP[0]][nextP[1]:]:
            idempty = ArrayMatrix[nextP[0]][nextP[1]:].index('.')
            idblock = ArrayMatrix[nextP[0]][nextP[1]:].index('#')
            if idempty<idblock:
                ArrayMatrix[nextP[0]][nextP[1]] = '.'
                ArrayMatrix_flip[nextP[1]][nextP[0]] = '.'
                ArrayMatrix[nextP[0]][nextP[1] + idempty] = '['
                ArrayMatrix_flip[nextP[1] + idempty][nextP[0]] = '['
                for k in range(nextP[1]+1,nextP[1]+idempty+1):
                    if ArrayMatrix[nextP[0]][k] == ']':
                        ArrayMatrix[nextP[0]][k] = '['
                        ArrayMatrix_flip[k][nextP[0]] = '['
                    else:
                        ArrayMatrix[nextP[0]][k] = ']'
                        ArrayMatrix_flip[k][nextP[0]] = ']'
                currP = nextP
        elif move == '<' and '.' in ArrayMatrix[nextP[0]][:nextP[1]]:
            idempty = ArrayMatrix[nextP[0]][nextP[1]::-1].index('.')
            idblock = ArrayMatrix[nextP[0]][nextP[1]::-1].index('#')
            if idempty < idblock:
                ArrayMatrix[nextP[0]][nextP[1]] = '.'
                ArrayMatrix_flip[nextP[1]][nextP[0]] = '.'
                ArrayMatrix[nextP[0]][nextP[1]-idempty] = ']'
                ArrayMatrix_flip[nextP[1]-idempty][nextP[0]] = ']'
                for k in range(nextP[1]-1,nextP[1]-idempty-1,-1):
                    if ArrayMatrix[nextP[0]][k] == ']':
                        ArrayMatrix[nextP[0]][k] = '['
                        ArrayMatrix_flip[k][nextP[0]] = '['
                    else:
                        ArrayMatrix[nextP[0]][k] = ']'
                        ArrayMatrix_flip[k][nextP[0]] = ']'
                currP = nextP
        elif (move == '^' and '.' in ArrayMatrix_flip[nextP[1]][:nextP[0]]) or \
                (move == 'v' and '.' in ArrayMatrix_flip[nextP[1]][nextP[0]:]):
            if ArrayMatrix[nextP[0]][nextP[1]] == '[':
                box = [nextP, [nextP[0],nextP[1]+1]]
            else:
                box = [[nextP[0], nextP[1] - 1], nextP]
            if move == '^':
                d = -1
            else:
                d = 1
            M1 = copy.deepcopy(ArrayMatrix)
            M1_flip = copy.deepcopy(ArrayMatrix_flip)
            flag, M1, M1_flip = canMove([box],d,M1,M1_flip)
            if flag:
                ArrayMatrix = M1
                ArrayMatrix_flip = M1_flip
                ArrayMatrix[box[0][0]][box[0][1]] = '.'
                ArrayMatrix[box[1][0]][box[1][1]] = '.'
                ArrayMatrix_flip[box[0][1]][box[0][0]] = '.'
                ArrayMatrix_flip[box[1][1]][box[1][0]] = '.'
                currP = nextP

tot = 0
for i in range(len(ArrayMatrix)):
    for j in range(len(ArrayMatrix[0])):
        if ArrayMatrix[i][j] == '[':
            tot += 100*i+j
print(tot)
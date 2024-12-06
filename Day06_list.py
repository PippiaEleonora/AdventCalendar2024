import numpy as np
from tqdm import tqdm

def follow_the_path(numberArray, numberArray_flip, Position, direction):
    n = len(numberArray)
    m = len(numberArray[0])
    
    Coverage = np.zeros([n,m])
    AllPosition = [(Position.copy(), direction)]
    # Position = StartPosition
    
    exit_board = 0
    isLoop = 0
    while not exit_board:
        if direction == '^':
            if sum(numberArray_flip[Position[1]][0:Position[0]])>0:
                # Find block
                idMax = Position[0] - (numberArray_flip[Position[1]][Position[0]-1::-1]).index(1) -1
                
                # Add coverage
                Coverage[idMax+1:Position[0]+1,Position[1]] = 1
                    
                # Change position/direction
                Position[0] = idMax + 1
                direction = '>'
                if (Position, direction) in AllPosition:
                    isLoop = 1
                    exit_board = 1
                else:
                    AllPosition.append((Position.copy(), direction))
            else:
                # Add coverage
                Coverage[0:Position[0]+1,Position[1]] = 1
                # Exit condition
                exit_board = 1
        elif direction == 'v':
            if sum(numberArray_flip[Position[1]][Position[0]:])>0:
                # Find block
                idMin = (numberArray_flip[Position[1]][Position[0]:]).index(1) + Position[0]
                
                # Add coverage
                Coverage[Position[0]:idMin,Position[1]] = 1
                    
                # Change position/direction
                Position[0] = idMin-1
                direction = '<'
                if (Position, direction) in AllPosition:
                    isLoop = 1
                    exit_board = 1
                else:
                    AllPosition.append((Position.copy(), direction))
            else:
                # Add coverage
                Coverage[Position[0]:,Position[1]] = 1
                # Exit condition
                exit_board = 1
        elif direction == '>':
            if sum(numberArray[Position[0]][Position[1]:])>0:
                # Find block
                idMin = (numberArray[Position[0]][Position[1]:]).index(1) + Position[1]
                
                # Add coverage
                Coverage[Position[0],Position[1]:idMin] = 1
                    
                # Change position/direction
                Position[1] = idMin - 1
                direction = 'v'
                if (Position, direction) in AllPosition:
                    isLoop = 1
                    exit_board = 1
                else:
                    AllPosition.append((Position.copy(), direction))
            else:
                # Add coverage
                Coverage[Position[0],Position[1]:] = 1
                # Exit condition
                exit_board = 1
        elif direction == '<':
            if sum(numberArray[Position[0]][0:Position[1]])>0:
                # Find block
                idMax = Position[1] - numberArray[Position[0]][Position[1]-1::-1].index(1) -1
                
                # Add coverage
                Coverage[Position[0],idMax+1:Position[1]+1] = 1
                    
                # Change position/direction
                Position[1] = idMax + 1
                direction = '^'
                if (Position, direction) in AllPosition:
                    isLoop = 1
                    exit_board = 1
                else:
                    AllPosition.append((Position.copy(), direction))
            else:
                # Add coverage
                Coverage[Position[0],0:Position[1]+1] = 1
                # Exit condition
                exit_board = 1
    return Coverage, isLoop

if __name__ == '__main__':
    with open('Input06.txt') as f:
        arrayRaw = f.readlines()
     
numberArray = []   
numberArray_flip = [] 
StartPosition = [0,0]
direction = '^'
for i in range(len(arrayRaw)):
    line = arrayRaw[i]
    numberArray.append([1 if l=='#' else 0 for l in line.replace('\n','')])
    for l in range(len(line.replace('\n',''))):
        if line[l]=='#':
            if i==0:
                numberArray_flip.append([1])
            else:
                numberArray_flip[l].append(1)
        else:
            if i==0:
                numberArray_flip.append([0])
            else:
                numberArray_flip[l].append(0)
    if '^' in line:
        StartPosition[0] = i # line
        StartPosition[1] = line.index('^') # column

Matrix = np.matrix(numberArray)

# First star
Coverage, isLoop = follow_the_path(numberArray, numberArray_flip, StartPosition.copy(), direction)
print(sum(sum(Coverage)))

# Second star
count = 0
for i in tqdm(range(len(numberArray))):
    for j in range(len(numberArray[0])):
        if numberArray[i][j] == 0 and not [i,j]==StartPosition:
            numberArray[i][j] = 1
            numberArray_flip[j][i] = 1
            Coverage, isLoop = follow_the_path(numberArray, numberArray_flip, StartPosition.copy(), direction)
            if isLoop:
                count += 1
            numberArray[i][j] = 0
            numberArray_flip[j][i] = 0

print(count)

# With .index() takes 00:00:16
# With np.where() takes 00:06:18         
    
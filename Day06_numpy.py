import numpy as np
from tqdm import tqdm

def follow_the_path(Matrix, Position, direction):
    n = Matrix.shape[0]
    m = Matrix.shape[1]
    
    Coverage = np.zeros([n,m])
    AllPosition = [(Position.copy(), direction)]
    # Position = StartPosition
    
    exit_board = 0
    isLoop = 0
    while not exit_board:
        if direction == '^':
            if sum(Matrix[0:Position[0],Position[1]])>0:
                # Find block
                idMax = np.where(Matrix[0:Position[0],Position[1]])[0][-1]
                
                # Add coverage
                for i in range(idMax+1,Position[0]+1):
                    Coverage[i,Position[1]] = 1
                    
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
                for i in range(Position[0]+1):
                    Coverage[i,Position[1]] = 1
                # Exit condition
                exit_board = 1
        elif direction == 'v':
            if sum(Matrix[Position[0]:,Position[1]])>0:
                # Find block
                idMin = np.where(Matrix[Position[0]:,Position[1]])[0][0] + Position[0]
                
                # Add coverage
                for i in range(Position[0],idMin):
                    Coverage[i,Position[1]] = 1
                    
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
                for i in range(Position[0],n):
                    Coverage[i,Position[1]] = 1
                # Exit condition
                exit_board = 1
        elif direction == '>':
            if np.sum(Matrix[Position[0],Position[1]:],axis=1)>0:
                # Find block
                idMin = np.where(Matrix[Position[0],Position[1]:])[1][0] + Position[1]
                
                # Add coverage
                for i in range(Position[1],idMin):
                    Coverage[Position[0],i] = 1
                    
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
                for i in range(Position[1],m):
                    Coverage[Position[0],i] = 1
                # Exit condition
                exit_board = 1
        elif direction == '<':
            if np.sum(Matrix[Position[0],0:Position[1]],axis=1)>0:
                # Find block
                idMax = np.where(Matrix[Position[0],0:Position[1]])[1][-1]
                
                # Add coverage
                for i in range(idMax+1,Position[1]+1):
                    Coverage[Position[0],i] = 1
                    
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
                for i in range(Position[1]+1):
                    Coverage[Position[0],i] = 1
                # Exit condition
                exit_board = 1
    return Coverage, isLoop
if __name__ == '__main__':
    with open('Input06.txt') as f:
        arrayRaw = f.readlines()
     
numberArray = []   
StartPosition = [0,0]
direction = '^'
for i in range(len(arrayRaw)):
    line = arrayRaw[i]
    numberArray.append([1 if l=='#' else 0 for l in line.replace('\n','')])
    if '^' in line:
        StartPosition[0] = i # line
        StartPosition[1] = line.index('^') # column

Matrix = np.matrix(numberArray)

# First star
Coverage, isLoop = follow_the_path(Matrix, StartPosition.copy(), direction)
print(sum(sum(Coverage)))


count = 0
print(Matrix.shape)
for i in tqdm(range(Matrix.shape[0])):
    for j in range(Matrix.shape[0]):
        if Matrix[i,j] == 0 and not [i,j]==StartPosition:
            Matrix[i,j] = 1
            Coverage, isLoop = follow_the_path(Matrix, StartPosition.copy(), direction)
            if isLoop:
                count += 1
            Matrix[i,j] = 0

print(count)

# With np.where takes 00:06:18         
    
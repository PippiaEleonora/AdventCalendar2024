import math
from tqdm import tqdm
import numpy as np

def search_set(SetList,start):
    SetMember = np.zeros([n,m])
    visited = []
    queue = [start]
    SetMember[start[0],start[1]] = 1
    while len(queue)>0:
        node = queue.pop(0)
        visited.append(node)
        if [node[0]+1,node[1]] in SetList and not [node[0]+1,node[1]] in visited and not [node[0]+1,node[1]] in queue:
            SetMember[node[0]+1,node[1]] = 1
            queue.append([node[0]+1,node[1]])
        if [node[0]-1,node[1]] in SetList and not [node[0]-1,node[1]] in visited and not [node[0]-1,node[1]] in queue:
            SetMember[node[0]-1,node[1]] = 1
            queue.append([node[0]-1,node[1]])
        if [node[0],node[1]+1] in SetList and not [node[0],node[1]+1] in visited and not [node[0],node[1]+1] in queue:
            SetMember[node[0],node[1]+1] = 1
            queue.append([node[0],node[1]+1])
        if [node[0],node[1]-1] in SetList and not [node[0],node[1]-1] in visited and not [node[0],node[1]-1] in queue:
            SetMember[node[0],node[1]-1] = 1
            queue.append([node[0],node[1]-1])
    return SetMember, visited
            

if __name__ == '__main__':
    with open('Input12.txt') as f:
        arrayRaw = f.readlines()
     
arrayRaw = [a.replace('\n','') for a in arrayRaw]   
n = len(arrayRaw)
m = len(arrayRaw[0])

V = ''.join(arrayRaw)
letters = list(set(V))
Dictionary = dict(zip(letters, [[]]*len(letters)))
Matrix = np.zeros([n,m])

Perimeters = np.zeros([n,m])
for i in range(n):
    for j in range(m):
        Matrix[i,j] = letters.index(arrayRaw[i][j])
        if Dictionary[arrayRaw[i][j]] == []:
            Dictionary[arrayRaw[i][j]] = [[i,j]]
        else:
            Dictionary[arrayRaw[i][j]].append([i,j])
        if i<n-1:
            if not arrayRaw[i][j] == arrayRaw[i+1][j]:
                Perimeters[i,j] += 1
        else:
            Perimeters[i,j] += 1
        
        if j<m-1:
            if not arrayRaw[i][j] == arrayRaw[i][j+1]:
                Perimeters[i,j] += 1
        else:
            Perimeters[i,j] += 1
            
        if i>0:
            if not arrayRaw[i][j] == arrayRaw[i-1][j]:
                Perimeters[i,j] += 1
        else:
            Perimeters[i,j] += 1
        
        if j>0:
            if not arrayRaw[i][j] == arrayRaw[i][j-1]:
                Perimeters[i,j] += 1
        else:
            Perimeters[i,j] += 1

Vertices = np.zeros([n,m])
for i in range(n):
    for j in range(m):
        if i<n-1 and j<m-1:
            if not arrayRaw[i][j] == arrayRaw[i][j+1] and not arrayRaw[i][j] == arrayRaw[i+1][j]: #and not arrayRaw[i][j] == arrayRaw[i+1][j+1]
                Vertices[i,j] += 1
            elif arrayRaw[i][j] == arrayRaw[i][j+1] and not arrayRaw[i][j] == arrayRaw[i+1][j+1] and arrayRaw[i][j] == arrayRaw[i+1][j]:
                Vertices[i,j] += 1
        elif j<m-1 and not arrayRaw[i][j] == arrayRaw[i][j+1]:
            Vertices[i,j] += 1
        elif i<n-1 and not arrayRaw[i][j] == arrayRaw[i+1][j]:
            Vertices[i,j] += 1
        elif i==n-1 and j==m-1:
            Vertices[i,j] += 1
            
        if i<n-1 and j>0:
            if not arrayRaw[i][j] == arrayRaw[i][j-1] and not arrayRaw[i][j] == arrayRaw[i+1][j]: # and not arrayRaw[i][j] == arrayRaw[i+1][j-1]
                Vertices[i,j] += 1
            elif arrayRaw[i][j] == arrayRaw[i][j-1] and not arrayRaw[i][j] == arrayRaw[i+1][j-1] and arrayRaw[i][j] == arrayRaw[i+1][j]:
                Vertices[i,j] += 1
        elif j>0 and not arrayRaw[i][j] == arrayRaw[i][j-1]:
            Vertices[i,j] += 1
        elif i<n-1 and not arrayRaw[i][j] == arrayRaw[i+1][j]:
            Vertices[i,j] += 1
        elif i==n-1 and j==0:
            Vertices[i,j] += 1
            
        if i>0 and j<m-1:
            if not arrayRaw[i][j] == arrayRaw[i][j+1] and not arrayRaw[i][j] == arrayRaw[i-1][j]: # and not arrayRaw[i][j] == arrayRaw[i-1][j+1]
                Vertices[i,j] += 1
            elif arrayRaw[i][j] == arrayRaw[i][j+1] and not arrayRaw[i][j] == arrayRaw[i-1][j+1] and arrayRaw[i][j] == arrayRaw[i-1][j]:
                Vertices[i,j] += 1
        elif j<m-1 and not arrayRaw[i][j] == arrayRaw[i][j+1]:
            Vertices[i,j] += 1
        elif i>0 and not arrayRaw[i][j] == arrayRaw[i-1][j]:
            Vertices[i,j] += 1
        elif i==0 and j==m-1:
            Vertices[i,j] += 1
            
        if i>0 and j>0:
            if not arrayRaw[i][j] == arrayRaw[i][j-1] and not arrayRaw[i][j] == arrayRaw[i-1][j]: # and not arrayRaw[i][j] == arrayRaw[i-1][j-1]
                Vertices[i,j] += 1
            elif arrayRaw[i][j] == arrayRaw[i][j-1] and not arrayRaw[i][j] == arrayRaw[i-1][j-1] and arrayRaw[i][j] == arrayRaw[i-1][j]:
                Vertices[i,j] += 1
        elif j>0 and not arrayRaw[i][j] == arrayRaw[i][j-1]:
            Vertices[i,j] += 1
        elif i>0 and not arrayRaw[i][j] == arrayRaw[i-1][j]:
            Vertices[i,j] += 1        
        elif i==0 and j==0:
            Vertices[i,j] += 1

tot_FirstStar = 0
tot_SecondStar = 0
for l in tqdm(letters):
    SetOfPoints = Dictionary[l]
    while len(SetOfPoints)>0:
        MatrixMember, ListMember = search_set(SetOfPoints,SetOfPoints[0])
        tot_FirstStar += np.sum(MatrixMember)*np.sum(np.multiply(MatrixMember,Perimeters))
        tot_SecondStar += np.sum(MatrixMember)*np.sum(np.multiply(MatrixMember,Vertices))
        Dictionary[l] = [s for s in SetOfPoints if not s in ListMember]
        SetOfPoints = Dictionary[l]

        
print(tot_FirstStar)
print(tot_SecondStar)
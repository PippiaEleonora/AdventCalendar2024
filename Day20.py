import numpy as np
import copy
from tqdm import tqdm
from collections import deque
#Thanks to https://github.com/mgtezak/ for part2

def find_Glitch(path,threshold,distanceMax):
    cheats = 0
    for t2 in range(threshold, len(path)):
        for t1 in range(t2 - threshold):
            x1, y1 = path[t1]
            x2, y2 = path[t2]
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance <= distanceMax and t2 - t1 - distance >= threshold:
                cheats += 1
    return cheats

def find_MinPath(Walls,startP,endP,n):
    visited = []
    queue = deque([(startP,[])])
    Cost = np.zeros([n, n])
    while queue:
        curr,Path = queue.popleft()
        visited.append(curr)
        Path.append(curr)
        if curr == endP:
            return Cost,Path
        Next = [[curr[0]+1,curr[1]],[curr[0],curr[1]+1],[curr[0]-1,curr[1]],[curr[0],curr[1]-1]]
        for node in Next:
            if node[0]<n and node[0]>-1 and node[1]<n and node[1]>-1:
                if not Walls[node[0],node[1]]:
                    if (Cost[node[0],node[1]] == 0 and not node==startP) or Cost[node[0],node[1]]>Cost[curr[0],curr[1]]+1:
                        Cost[node[0], node[1]] = Cost[curr[0],curr[1]]+1
                        if not node in visited:
                            queue.append((node,Path.copy()))
    return Cost,Path



if __name__ == '__main__':
    with open('Input20.txt') as f:
        arrayRaw = f.readlines()


n = len(arrayRaw)
Walls = np.zeros([n,n])
ListWalls = []
for i in range(n):
    line = arrayRaw[i].replace('\n','')
    for j in range(n):
        if line[j] == '#':
            Walls[i,j] = 1
            if i>0 and i<n-1 and j>0 and j<n-1:
                ListWalls.append([i,j])
        elif line[j] == 'E':
            endP = [i,j]
        elif line[j] == 'S':
            startP = [i,j]

Cost,Path = find_MinPath(Walls,startP,endP,n)
print(Cost[endP[0],endP[1]])

#FisrtStar
tot = find_Glitch(Path,100,2)
print(tot)

#SecondStar
tot = find_Glitch(Path,100,20)
print(tot)
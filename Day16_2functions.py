
import os
import re
import math
import numpy as np

def find_AllMinPath(Walls,startP,startDir,endP,n,Cost):
    visited = []
    path = set([(startP[0],startP[1])])
    queue = [[startP,startDir,0,path]]
    PathMatrix = {str(startP): path}
    while len(queue)>0:
        curr = queue.pop(0)
        visited.append(curr)
        startDir = curr[1]
        cost_node = curr[2]
        curr_path = curr[3]
        curr = curr[0]

        if not curr == endP:
            Next = [[curr[0]+1,curr[1]],[curr[0],curr[1]+1],[curr[0]-1,curr[1]],[curr[0],curr[1]-1]]
            Direction = ['v', '>', '^', '<']
            for node,dir in zip(Next,Direction):
                if startDir == dir:
                    if node[0] < n and node[0] > -1 and node[1] < n and node[1] > -1 and not Walls[node[0], node[1]]:
                        if Cost[node[0], node[1]] == cost_node + 1:
                            path = curr_path.union(set([(node[0], node[1])]))
                            if str(node) in list(PathMatrix):
                                path = path.union(PathMatrix[str(node)])
                            PathMatrix[str(node)] = path
                            queue.append([node, dir, Cost[node[0], node[1]], path])
                        elif Cost[node[0], node[1]]+1000 >= cost_node + 1:
                            path = curr_path.union(set([(node[0], node[1])]))
                            queue.append([node, dir, cost_node + 1, path])
                elif not startDir+dir in ['<>','><', '^v', 'v^']:
                    if node[0]<n and node[0]>-1 and node[1]<n and node[1]>-1 and not Walls[node[0],node[1]]:
                        if Cost[node[0], node[1]] == cost_node + 1001:
                            path = curr_path.union(set([(node[0], node[1])]))
                            if str(node) in list(PathMatrix):
                                path = path.union(PathMatrix[str(node)])
                            PathMatrix[str(node)] = path
                            queue.append([node, dir, Cost[node[0], node[1]], path])
    return PathMatrix

def find_MinPath(Walls,startP,startDir,endP,n):
    visited = []
    queue = [[startP,startDir,0]]
    Cost = np.zeros([n, n])
    while len(queue)>0:
        curr = queue.pop(0)
        visited.append(curr)
        startDir = curr[1]
        cost_node = curr[2]
        curr = curr[0]

        if not curr == endP:
            Next = [[curr[0]+1,curr[1]],[curr[0],curr[1]+1],[curr[0]-1,curr[1]],[curr[0],curr[1]-1]]
            Direction = ['v', '>', '^', '<']
            for node,dir in zip(Next,Direction):
                if startDir == dir:
                    if node[0] < n and node[0] > -1 and node[1] < n and node[1] > -1 and not Walls[node[0], node[1]]:
                        if (Cost[node[0], node[1]] == 0 and not node == startP) or Cost[node[0], node[1]] > cost_node + 1:
                            Cost[node[0], node[1]] = cost_node + 1
                            if not [node,dir,Cost[node[0], node[1]]] in visited:
                                queue.append([node,dir,Cost[node[0], node[1]]])
                elif not startDir+dir in ['<>','><', '^v', 'v^']:
                    if node[0]<n and node[0]>-1 and node[1]<n and node[1]>-1 and not Walls[node[0],node[1]]:
                        if (Cost[node[0],node[1]] == 0 and not node==startP) or Cost[node[0],node[1]]>cost_node+1001:
                            Cost[node[0], node[1]] = cost_node+1001
                            if not [node,dir,Cost[node[0], node[1]]] in visited:
                                queue.append([node, dir, Cost[node[0], node[1]]])
    return Cost

if __name__ == '__main__':
    with open('Input16.txt') as f:
        arrayRaw = f.readlines()


n = len(arrayRaw)

Walls = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        if arrayRaw[i][j] == '#':
            Walls[i,j] = 1
    if 'S' in arrayRaw[i]:
        StartPoint = [i,arrayRaw[i].index('S')]
    if 'E' in arrayRaw[i]:
        EndPoint = [i,arrayRaw[i].index('E')]

Score = find_MinPath(Walls,StartPoint,'>',EndPoint,n)
print(Score[EndPoint[0],EndPoint[1]])

PathMatrix = find_AllMinPath(Walls,StartPoint,'>',EndPoint,n,Score)
fullPath = PathMatrix[str(EndPoint)]
print(len(fullPath))


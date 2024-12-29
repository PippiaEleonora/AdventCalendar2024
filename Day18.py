import numpy as np

def find_MinPath(Walls,startP,endP,n):
    visited = []
    queue = [startP]
    Cost = np.zeros([n, n])
    while len(queue)>0:
        curr = queue.pop(0)
        visited.append(curr)
        if curr == endP:
            return Cost[curr[0],curr[1]]
        Next = [[curr[0]+1,curr[1]],[curr[0],curr[1]+1],[curr[0]-1,curr[1]],[curr[0],curr[1]-1]]
        for node in Next:
            if node[0]<n and node[0]>-1 and node[1]<n and node[1]>-1 and not Walls[node[0],node[1]]:
                if (Cost[node[0],node[1]] == 0 and not node==startP) or Cost[node[0],node[1]]>Cost[curr[0],curr[1]]+1:
                    Cost[node[0], node[1]] = Cost[curr[0],curr[1]]+1
                    if not node in visited:
                        queue.append(node)
    return -1



if __name__ == '__main__':
    with open('Input18.txt') as f:
        arrayRaw = f.readlines()


n = 71
currVal = 1024 #1348
Walls = np.zeros([n,n])
for l in range(currVal):
    line = arrayRaw[l].replace('\n','').split(',')
    Walls[int(line[0]),int(line[1])] = 1

startP = [0,0]
endP = [70,70]

minCost = find_MinPath(Walls,startP,endP,n)
print(minCost)


print(len(arrayRaw))
currVal = 2900
Walls = np.zeros([n,n])
for l in range(currVal):
    line = arrayRaw[l].replace('\n','').split(',')
    Walls[int(line[0]), int(line[1])] = 1
reach = 1
while reach:
    line = arrayRaw[currVal].replace('\n','').split(',')
    Walls[int(line[0]),int(line[1])] = 1

    startP = [0,0]
    endP = [70,70]

    minCost = find_MinPath(Walls,startP,endP,n)

    if minCost == -1:
        reach = 0
        print(currVal)
        print(line)
    else:
        currVal += 1
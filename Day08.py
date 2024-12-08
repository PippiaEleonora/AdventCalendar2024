import numpy as np            
if __name__ == '__main__':
    with open('Input08.txt') as f:
        arrayRaw = f.readlines()

Dictionary ={'0': []}
for i in range(len(arrayRaw)):
    line = arrayRaw[i].replace('\n','')
    for j in range(len(line)):
        if not line[j]=='.':
            if line[j] in Dictionary.keys():
                Dictionary[line[j]].append([i,j])
            else:
                Dictionary.update({line[j]: [[i,j]]})
                
n = len(arrayRaw)
m = len(arrayRaw[0])-1

#First star   
Antinodes = np.zeros((n,m))
for k in Dictionary:
        antenne = Dictionary[k]
        for i in range(len(antenne)):
            for j in range(i+1,len(antenne)):
                x3 = antenne[j][0] + (antenne[j][0]-antenne[i][0])
                y3 = antenne[j][1] + (antenne[j][1]-antenne[i][1])
                x4 = antenne[i][0] + (antenne[i][0]-antenne[j][0])
                y4 = antenne[i][1] + (antenne[i][1]-antenne[j][1])
                if x3>=0 and x3<n and y3>=0 and y3<m:
                    Antinodes[x3,y3] = 1
                if x4>=0 and x4<n and y4>=0 and y4<m:   
                    Antinodes[x4,y4] = 1
            
print(sum(sum(Antinodes)))         

#Second Star
Antinodes = np.zeros((n,m))
for k in Dictionary:
        antenne = Dictionary[k]
        for i in range(len(antenne)):
            for j in range(i+1,len(antenne)):
                dx = (antenne[j][0]-antenne[i][0])
                dy = (antenne[j][1]-antenne[i][1])
                x3 = antenne[j][0]
                y3 = antenne[j][1]
                while x3>=0 and x3<n and y3>=0 and y3<m:
                    Antinodes[x3,y3] = 1
                    x3 += dx
                    y3 += dy
                
                dx = (antenne[i][0]-antenne[j][0])
                dy = (antenne[i][1]-antenne[j][1])
                x4 = antenne[i][0]
                y4 = antenne[i][1]
                
                while x4>=0 and x4<n and y4>=0 and y4<m:   
                    Antinodes[x4,y4] = 1
                    x4 += dx
                    y4 += dy
            
print(sum(sum(Antinodes)))      
        

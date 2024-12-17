
import os
import re
import math
import numpy as np
if __name__ == '__main__':
    with open('Input14.txt') as f:
        arrayRaw = f.readlines()
        
Robots = [re.findall('-?[0-9]+',a) for a in arrayRaw]
Robots = [[float(r) for r in robot] for robot in Robots]
n = 101
m = 103

# First star
iteration = 100
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
for r in Robots:
    x = (r[0]+iteration*r[2])%n
    y = (r[1]+iteration*r[3])%m
    
    if x<math.floor(n/2):
        if y<math.floor(m/2):
            Q1 += 1
        elif y>math.floor(m/2):
            Q3 += 1
    elif x>math.floor(n/2):
        if y<math.floor(m/2):
            Q2 += 1
        elif y>math.floor(m/2):
            Q4 += 1

print(Q1*Q2*Q3*Q4)

# Second Star
save_path = os.getcwd()
file_name = "\Christmas_tree.txt"
completeName = save_path + file_name
with open(completeName, 'a') as file:
    for i in range(10000):
        Matrix = np.zeros([n,m])
        for r in Robots:
            x = (r[0]+i*r[2])%n
            y = (r[1]+i*r[3])%m
            Matrix[round(x),round(y)] = 1
        
        for k in range(50,n):
            if np.sum(Matrix[k,:])>32:
                # Save the matrix to a text file
                file.write('\n\n')
                np.savetxt(file, Matrix, fmt='%d')

print(Q1*Q2*Q3*Q4)
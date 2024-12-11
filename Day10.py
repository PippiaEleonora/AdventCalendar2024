def findNine(Matrix, startPosition,withRepetition):
    current = [startPosition]
    for val in range(1,10):
        new = []
        for c in current:
            if c[0]<n-1 and Matrix[c[0]+1][c[1]] == val and (withRepetition or not [c[0]+1,c[1]] in new):
                new.append([c[0]+1,c[1]])
            if c[0]>0 and Matrix[c[0]-1][c[1]] == val and (withRepetition or not [c[0]-1,c[1]] in new):
                new.append([c[0]-1,c[1]])
            if c[1]<m-1 and Matrix[c[0]][c[1]+1] == val and (withRepetition or not [c[0],c[1]+1] in new):
                new.append([c[0],c[1]+1])
            if c[1]>0 and Matrix[c[0]][c[1]-1] == val and (withRepetition or not [c[0],c[1]-1] in new):
                new.append([c[0],c[1]-1])
        current = new
    return current


if __name__ == '__main__':
    with open('Input10.txt') as f:
        arrayRaw = f.readlines()

Matrix = [[float(l) for l in line.replace('\n','')]for line in arrayRaw]
ListZero = []
n = len(Matrix)
m = len(Matrix[0])
for i in range(n):
    for j in range(m):
        if Matrix[i][j] == 0:
            ListZero.append([i,j])
       
# Fisrt star     
tot = 0
for startPosition in ListZero:
    final_nine = findNine(Matrix, startPosition,0)
    tot += len(final_nine)                       
                        
print(tot)

# Second star     
tot = 0
for startPosition in ListZero:
    final_nine = findNine(Matrix, startPosition,1)
    tot += len(final_nine)                       
                        
print(tot)
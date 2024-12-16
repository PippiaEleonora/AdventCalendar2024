
import re

def solve_sistem(A,B,val):
    # 94*X+22*Y = 8400
    # 24*X+67*Y = 5400

    # X = 8400/94 - 22*Y/94                     val[0]/A[0] - B[0]/A[0]*y
    # 24*8400/94 -24*22*Y/94 + 67*Y = 5400      (val[1]-A[1]*val[0]/A[0])/(B[1]-A[1]*B[0]/A[0])

    if abs(B[1] - A[1]*B[0]/A[0])>10**-5:
        y = (val[1]*A[0] - A[1]*val[0])/(B[1]*A[0] - A[1]*B[0])
        x = val[0]/A[0] - B[0]*y/A[0]

    else:
        print('ERROR!')
    
    return x,y


if __name__ == '__main__':
    with open('Input13.txt') as f:
        arrayRaw = f.readlines()

TotalString = ''.join(arrayRaw)
All_numbers = re.findall('[0-9]+',TotalString)
A_button = [[float(All_numbers[i]), float(All_numbers[i+1])] for i in range(0,len(All_numbers),6)]
B_button = [[float(All_numbers[i]),float(All_numbers[i+1])] for i in range(2,len(All_numbers),6)]
Prize = [[float(All_numbers[i]),float(All_numbers[i+1])] for i in range(4,len(All_numbers),6)]

# First Star
TotCost = 0
for i in range(len(A_button)):
    x,y = solve_sistem(A_button[i], B_button[i], Prize[i])
    if abs(x-round(x))<10**-5 and abs(y-round(y))<10**-5:
        TotCost += x*3+y

print(TotCost)
        
# Second Star
TotCost = 0
for i in range(len(A_button)):
    x,y = solve_sistem(A_button[i], B_button[i], [Prize[i][0]+10000000000000, Prize[i][1]+10000000000000])
    if abs(x-round(x))<10**-3 and abs(y-round(y))<10**-3:
        TotCost += x*3+y
        
print(TotCost)
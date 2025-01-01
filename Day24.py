import re
import copy
import itertools

def check_correctness(Original_Val, change=[]):
    Queue = list(Original_Val.keys())
    potential = []
    while len(Queue) > 0:
        arg = Queue.pop(0)
        if arg in list(Operations.keys()):
            for k in list(Operations[arg].keys()):
                if k in list(Original_Val.keys()):
                    for op in Operations[arg][k]:
                        if op[1] in change:
                            id = change.index(op[1])
                            if id>3:
                                op[1] = change[4-id]
                            else:
                                op[1] = change[4+id]
                        if not op[1] in list(Original_Val.keys()):
                            Queue.append(op[1])
                            x1 = int(Original_Val[arg])
                            x2 = int(Original_Val[k])
                            if op[0] == 'XOR':
                                Original_Val.update({op[1]: x1 ^ x2})
                            elif op[0] == 'OR':
                                Original_Val.update({op[1]: x1 or x2})
                            else:
                                Original_Val.update({op[1]: x1 and x2})
                        else:
                            x1 = int(Original_Val[arg])
                            x2 = int(Original_Val[k])
                            if op[0] == 'XOR':
                                if not (Original_Val[op[1]] == (x1 ^ x2)):
                                    potential += [arg,k]
                            elif op[0] == 'OR':
                                if not (Original_Val[op[1]] == (x1 or x2)):
                                    potential += [op[1]]
                            else:
                                if not (Original_Val[op[1]] == (x1 and x2)):
                                    potential += [op[1]]
    return potential,Original_Val
if __name__ == '__main__':
    with open('Input24.txt') as f:
        arrayRaw = f.readlines()

Values = {}
Operations = {}
Operations_string = ''
tot_op = 0
Variables = []
for line in arrayRaw:
    if '->' in line: #Operation
        tot_op += 1
        line = line.replace('\n','')
        line = line.split(' -> ')
        if 'XOR' in line[0]:
            line[0] = line[0].split(' XOR ')
            op = 'XOR'
        elif 'OR' in line[0]:
            line[0] = line[0].split(' OR ')
            op = 'OR'
        else:
            line[0] = line[0].split(' AND ')
            op = 'AND'

        if line[0][0] in list(Operations.keys()):
            if line[0][1] in list(Operations[line[0][0]].keys()):
                Operations[line[0][0]][line[0][1]].append([op, line[1]])
            else:
                Operations[line[0][0]].update({line[0][1]: [[op, line[1]]]})
        else:
            Operations.update({line[0][0]: {line[0][1]: [[op, line[1]]]}})
        if line[0][1] in list(Operations.keys()):
            if line[0][0] in list(Operations[line[0][1]].keys()):
                Operations[line[0][1]][line[0][0]].append([op, line[1]])
            else:
                Operations[line[0][1]].update({line[0][0]: [[op, line[1]]]})
        else:
            Operations.update({line[0][1]: {line[0][0]: [[op, line[1]]]}})
    elif ':' in line: #Values
        line = line.split(': ')
        Values.update({line[0]: int(line[1])})
        Variables.append(line[0])
Original_Val = copy.deepcopy(Values)

print('Tot operation:' + str(tot_op))
wrong = set()
Queue = list(Values.keys())
while len(Queue)>0:
    arg = Queue.pop(0)
    if arg in list(Operations.keys()):
        for k in list(Operations[arg].keys()):
            if k in list(Values.keys()):
                for op in Operations[arg][k]:
                    if not op[1] in Queue:
                        Queue.append(op[1])
                        x1 = int(Values[arg])
                        x2 = int(Values[k])
                        if op[0] == 'XOR':
                            Values.update({op[1]: x1^x2})
                        elif op[0] == 'OR':
                            Values.update({op[1]: x1 or x2})
                        else:
                            Values.update({op[1]: x1 and x2})

                        ## Not my code ##
                        if op[1][0] == "z" and op[0] != "XOR" and op[1] != 'z45':
                            wrong.add(op[1])
                        if (
                                op[0] == "XOR"
                                and op[1][0] not in ["x", "y", "z"]
                                and arg[0] not in ["x", "y", "z"]
                                and k[0] not in ["x", "y", "z"]
                        ):
                            wrong.add(op[1])
                        if op[0] == "AND" and "x00" not in [arg, k]:
                            for subarg in list(Operations.keys()):
                                for subk in list(Operations[subarg].keys()):
                                    for subop in Operations[subarg][subk]:
                                        if (op[1] == subarg or op[1] == subk) and subop[0] != "OR":
                                            wrong.add(op[1])
                        if op[0] == "XOR":
                            for subarg in list(Operations.keys()):
                                for subk in list(Operations[subarg].keys()):
                                    for subop in Operations[subarg][subk]:
                                        if (op[1] == subarg or op[1] == subk) and subop[0] == "OR":
                                            wrong.add(op[1])
                        ## end Not My Code ###

print(sorted(wrong))
Key = list(Values.keys())
Key.sort()
endIndex = int(Key[-1][1:])
Z_string = ''
for i in range(endIndex,-1,-1):
    if i<10:
        Z_string += str(Values['z0' + str(i)])
    else:
        Z_string += str(Values['z'+str(i)])
print(int(Z_string,2))
print(Z_string)
X_string = ''
Y_string = ''
for k in Key:
    if k[0] == 'x':
        X_string += str(Values[k])
    elif k[0] == 'y':
        Y_string += str(Values[k])

realZ = str(bin(int(X_string[-1::-1],2)+int(Y_string[-1::-1],2)))[2:]
print(realZ)

for i in range(endIndex+1):
    if not realZ[i] == Z_string[i]:
        print([45-i, realZ[i], Z_string[i]])

for i in range(endIndex+1):
    id = endIndex-i
    if id<10:
        Original_Val.update({'z0' + str(id): int(realZ[i])})
    else:
        Original_Val.update({'z' + str(id): int(realZ[i])})
potential,tempVal = check_correctness(copy.deepcopy(Original_Val))
potential = set(potential)
V = set(Variables)
S = potential.difference(V)
Set_one = []
Set_zero = []
for i in list(S):
    if tempVal[i] == 1:
        Set_one.append(i)
    else:
        Set_zero.append(i)

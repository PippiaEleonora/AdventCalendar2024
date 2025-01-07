import math

def calculate_program(Operations, RegisterA, RegisterB, RegisterC, star):
    id = 0
    running = 1
    out = []
    correct = 1
    while running and id<len(Operations):
        Op = [Operations[id],Operations[id+1]]
        ComboOperand = Op[1]
        if ComboOperand == 4:
            ComboOperand = RegisterA
        elif ComboOperand == 5:
            ComboOperand = RegisterB
        elif ComboOperand == 6:
            ComboOperand = RegisterC
            
        if Op[0] == 0: #Adv
            if RegisterA == 0:
                running = 0
            else:            
                RegisterA = RegisterA//(2**ComboOperand)
        elif Op[0] == 1: #bitwise XOR
            RegisterB = RegisterB^Op[1]
        elif Op[0] == 2:
            RegisterB = ComboOperand%8
        elif Op[0] == 3:
            if not RegisterA == 0:
                id = Op[1]-2
        elif Op[0] == 4:
            RegisterB = RegisterB^RegisterC
        elif Op[0] == 5:
            out.append(ComboOperand%8)
            if not out == Operations[0:len(out)]:
                correct = 0
                if star == 2:
                    running = 0
        elif Op[0] == 6:
            if RegisterA == 0:
                running = 0
            else:            
                RegisterB = RegisterA//(2**ComboOperand)
        elif Op[0] == 7:
            if RegisterA == 0:
                running = 0
            else:            
                RegisterC = RegisterA//(2**ComboOperand)
        id += 2
    return out,correct

def search_sequence(index,power):
    found = 0
    while not found:
        start_value = 0
        end_value = 0
        for i in range(len(index)):
            start_value += index[i]*8**(power-i-1)
        end_value = start_value+8**(power-len(index))+1
        temp_index = []
        for i in range(start_value,end_value):
            RegisterA = i
            out, correct = calculate_program(Operations, RegisterA, RegisterB, RegisterC, 1)
            if out == Operations[-power:]:
                print([i,out, bin(i)])
                if (RegisterA-start_value)//8**(power-1-len(index))<8:
                    temp_index.append((RegisterA-start_value)//8**(power-1-len(index)))
                # break
        power += 1
        temp_index = set(temp_index)
        if len(temp_index) == 1:
            index.append(list(temp_index)[0])
        elif len(temp_index) > 1:
            for s in range(len(temp_index)):
                new_index = index.copy() + [list(temp_index)[s]]
                print([new_index, power, temp_index])
                found = search_sequence(new_index,len(new_index)+4)
                if found:
                    break
            return found
        else:
            found = 0
            return 0
        if len(out) == n:
            return 1
    return found
            
if __name__ == '__main__':
    RegisterA = 64012472
    RegisterB = 0
    RegisterC = 0

    Operations = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]
    out = calculate_program(Operations, RegisterA, RegisterB, RegisterC, 1)

    print(out)
    # n = len(Operations)
    # min_val = 8**(n-1)
    # max_val = 8**n

    index = []
    power = 3
    search_sequence(index,power)
    
        
            
 
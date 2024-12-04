if __name__ == '__main__':
    with open('Input04.txt') as f:
        arrayRaw = f.readlines()
        
        
        
count = 0

# Vertical = []
# Rev_Vertical = []
# DiagonalSxDx = []
# Rev_DiagonalSxDx = []
# DiagonalDxSx = []
# Rev_DiagonalDxSx = []
Prosecution = [[],[],[],[],[],[]]
for l in range(len(arrayRaw)): #for each line
    line = arrayRaw[l]
    n = len(line)
    
    Positions = {'X': [], 'M': [], 'A': [], 'S': []}
    for i in range(n):
        if line[i] == 'X':
            Positions['X'].append(i)
        elif line[i] == 'M':
            Positions['M'].append(i)
        elif line[i] == 'A':
            Positions['A'].append(i)
        elif line[i] == 'S':
            Positions['S'].append(i)


    #Vertical Prosecution
    del_list = []
    for p in Prosecution[0]:
        if p[0] in Positions[p[1]]:
            if p[1] == 'S':
                count += 1
                del_list.append(p)
            elif p[1] == 'M':
                p[1] = 'A'
            else:
                p[1] = 'S'
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[0].remove(d)
    #Rev_Vertical Prosecution
    del_list = []
    for p in Prosecution[1]:
        if p[0] in Positions[p[1]]:
            if p[1] == 'X':
                count += 1
                del_list.append(p)
            elif p[1] == 'M':
                p[1] = 'X'
            else:
                p[1] = 'M'
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[1].remove(d)
    #DiagonalSxDx Prosecution
    del_list = []
    for p in Prosecution[2]:
        if p[0] in Positions[p[1]]:
            if p[1] == 'S':
                count += 1
                del_list.append(p)
            elif p[1] == 'M':
                p[0] += 1
                p[1] = 'A'
            else:
                p[0] += 1
                p[1] = 'S'
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[2].remove(d)
    #Rev_DiagonalSxDx Prosecution
    del_list = []
    for p in Prosecution[3]:
        if p[0] in Positions[p[1]]:
            if p[1] == 'X':
                count += 1
                del_list.append(p)
            elif p[1] == 'M':
                p[0] += 1
                p[1] = 'X'
            else:
                p[0] += 1
                p[1] = 'M'
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[3].remove(d)
    #DiagonalDxSx Prosecution
    del_list = []
    for p in Prosecution[4]:
        if p[0] in Positions[p[1]]:
            if p[1] == 'S':
                count += 1
                del_list.append(p)
            elif p[1] == 'M':
                p[0] -= 1
                p[1] = 'A'
            else:
                p[0] -= 1
                p[1] = 'S'
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[4].remove(d)
    #Rev_DiagonalDxSx Prosecution
    del_list = []
    for p in Prosecution[5]:
        if p[0] in Positions[p[1]]:
            if p[1] == 'X':
                count += 1
                del_list.append(p)
            elif p[1] == 'M': 
                p[0] -= 1
                p[1] = 'X'
            else:
                p[0] -= 1
                p[1] = 'M'
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[5].remove(d)
    
    
    # New starts
    for i in Positions['X']:
        #Horizontal count
        if (i+3<n) and (i+1 in Positions['M']) and (i+2 in Positions['A']) and (i+3 in Positions['S']):
            count += 1
        if i<n-3:
            Prosecution[2].append([i+1,'M']) #DiagonalSxDx
        if i>2:
            Prosecution[4].append([i-1,'M']) #DiagonalDxSx
        Prosecution[0].append([i,'M']) #Vertical
    
    # New starts Reverse
    for i in Positions['S']:
        #Rev Horizontal count
        if (i+3<n) and (i+1 in Positions['A']) and (i+2 in Positions['M']) and (i+3 in Positions['X']):
            count += 1
        if i<n-3:
            Prosecution[3].append([i+1,'A']) #DiagonalSxDx
        if i>2:
            Prosecution[5].append([i-1,'A']) #DiagonalDxSx
        Prosecution[1].append([i,'A']) #Vertical
        
print(count)
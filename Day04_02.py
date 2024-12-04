if __name__ == '__main__':
    with open('Input04.txt') as f:
        arrayRaw = f.readlines()
        
count = 0

# M . M     M . S       S . S       S . M
# . A .     . A .       . A .       . A .
# S . S     M . S       M . M       S . M
Prosecution = [[],[],[],[]]

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
            
    # M . M
    # . A .
    # S . S
    del_list = []
    for p in Prosecution[0]:
        if p[0] in Positions[p[1]]:
            if len(p)>2:
                del_list.append(p)
                if p[2] in Positions[p[3]]:
                    count += 1
            else:
                p[0] -= 1
                p[1] = 'S'
                p.append(p[0]+2)
                p.append('S')
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[0].remove(d)
        
    # M . S
    # . A .
    # M . S
    del_list = []
    for p in Prosecution[1]:
        if p[0] in Positions[p[1]]:
            if len(p)>2:
                del_list.append(p)
                if p[2] in Positions[p[3]]:
                    count += 1
            else:
                p[0] -= 1
                p[1] = 'M'
                p.append(p[0]+2)
                p.append('S')
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[1].remove(d)
        
    # S . S
    # . A .
    # M . M
    del_list = []
    for p in Prosecution[2]:
        if p[0] in Positions[p[1]]:
            if len(p)>2:
                del_list.append(p)
                if p[2] in Positions[p[3]]:
                    count += 1
            else:
                p[0] -= 1
                p[1] = 'M'
                p.append(p[0]+2)
                p.append('M')
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[2].remove(d)
    
    # S . M
    # . A .
    # S . M
    del_list = []
    for p in Prosecution[3]:
        if p[0] in Positions[p[1]]:
            if len(p)>2:
                del_list.append(p)
                if p[2] in Positions[p[3]]:
                    count += 1
            else:
                p[0] -= 1
                p[1] = 'S'
                p.append(p[0]+2)
                p.append('M')
        else:
            del_list.append(p)
    for d in del_list:
        Prosecution[3].remove(d)
        
    
    # New starts
    for i in Positions['M']:
        if i+2<n and i+2 in Positions['M']:
            Prosecution[0].append([i+1, 'A'])
        elif i+2<n and i+2 in Positions['S']:
            Prosecution[1].append([i+1, 'A'])
    for i in Positions['S']:
        if i+2<n and i+2 in Positions['S']:
            Prosecution[2].append([i+1, 'A'])
        elif i+2<n and i+2 in Positions['M']:
            Prosecution[3].append([i+1, 'A'])
    
print(count)
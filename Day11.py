import math
from tqdm import tqdm
if __name__ == '__main__':
    with open('Input11.txt') as f:
        arrayRaw = f.readlines()

line = arrayRaw[0].replace('\n','').split(' ')
Stones = [float(l) for l in line]
repetition = [1 for l in line]
for i in (range(75)):
    new = []
    new_rep = []
    for s in range(len(Stones)):
        
        if Stones[s] == 0:
            if not 1 in new:
                new.append(1)
                new_rep.append(repetition[s])
            else:
                new_rep[new.index(1)] += repetition[s]
        else:
            decimal = math.floor(math.log10(Stones[s]))+1
            if decimal%2:
                if not Stones[s]*2024 in new:
                    new.append(Stones[s]*2024)
                    new_rep.append(repetition[s])
                else:
                    new_rep[new.index(Stones[s]*2024)] += repetition[s]
            else:
                val1 = math.floor(Stones[s]/(10**(decimal/2)))
                val2 = Stones[s] - val1*(10**(decimal/2))
                if not val1 in new:
                    new.append(val1)
                    new_rep.append(repetition[s])
                else:
                    new_rep[new.index(val1)] += repetition[s]
                if not val2 in new:
                    new.append(val2)
                    new_rep.append(repetition[s])
                else:
                    new_rep[new.index(val2)] += repetition[s]
    Stones = new
    repetition = new_rep   
print(sum(repetition))
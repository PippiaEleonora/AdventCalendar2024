import numpy as np
from tqdm import tqdm
def MonkeyExcange(val):
    x = val*64
    val = val^x
    val = val % 16777216
    x = val//32
    val = val ^ x
    val = val % 16777216
    x = val*2048
    val = val ^ x
    val = val % 16777216
    return val

if __name__ == '__main__':
    with open('Input22.txt') as f:
        arrayRaw = f.readlines()

Numbers = []
for l in arrayRaw:
    Numbers.append(int(l.replace('\n','')))

iteration = 2000
Price = np.zeros([len(Numbers),iteration])
Changes = []
for i in range(iteration):
    for n in range(len(Numbers)):
        Numbers[n] = MonkeyExcange(Numbers[n])
        Price[n, i] = Numbers[n] % 10
        if i == 0:
            Changes.append(',')
        else:
            Changes[n] += str(Price[n, i] - Price[n, i-1])+','

print(sum(Numbers))


best = 0
seq_visited = []
for m in tqdm(range(len(Numbers))):
    Sequence = Changes[m].split(',')
    for i in range(iteration-4):
        tot = 0
        curr = ','.join(Sequence[i:i+4])
        curr = ','+curr
        if not curr in seq_visited:
            seq_visited.append(curr)
            for n in range(m,len(Numbers)):
                if curr in Changes[n]:
                    startId = Changes[n].index(curr)
                    seq = Changes[n][0:startId].split(',')
                    tot += Price[n, len(seq)+3]
            if tot > best:
                best = tot
                best_sequence = curr
    print(best_sequence)
    print(best)
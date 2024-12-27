from tqdm import tqdm

def movement(string):
    out = []
    dictionary ={
    'A': {'A': 'A', '^': '<A', '>': 'vA', 'v': '<vA', '<': 'v<<A'}, 
    '^': {'A': '>A', '^': 'A', '>': 'v>A', 'v': 'vA', '<': 'v<A'},
    '>': {'A': '^A', '^': '<^A', '>': 'A', 'v': '<A', '<': '<<A'},
    'v': {'A': '^>A', '^': '^A', '>': '>A', 'v': 'A', '<': '<A'},
    '<': {'A': '>>^A', '^': '>^A', '>': '>>A', 'v': '>A', '<': 'A'}}

    
    curr = 'A'
    for s in string:
        out.append(dictionary[curr][s])
        curr = s
    return out
    
def movement_optimized(string):
    out = {}
    dictionary ={
    'A': {'A': 'A', '^': '<A', '>': 'vA', 'v': '<vA', '<': 'v<<A'}, 
    '^': {'A': '>A', '^': 'A', '>': 'v>A', 'v': 'vA', '<': 'v<A'},
    '>': {'A': '^A', '^': '<^A', '>': 'A', 'v': '<A', '<': '<<A'},
    'v': {'A': '^>A', '^': '^A', '>': '>A', 'v': 'A', '<': '<A'},
    '<': {'A': '>>^A', '^': '>^A', '>': '>>A', 'v': '>A', '<': 'A'}}
    
    
    for k in list(string.keys()):
        curr = 'A'
        for s in k:
            if not dictionary[curr][s] in out.keys():
                out.update({dictionary[curr][s]: string[k]})
            else:
                out[dictionary[curr][s]] += string[k]
            curr = s
    return out

if __name__ == '__main__':
    
    #First star
    star = 2
    #Second star
    star = 25
    
    Input = [789, 968, 286, 349, 170]
    String_input = ['^^^<<A>A>AvvvA',
                                '^^^AvA<^Avvv>A',
                                '<^A^^Av>AvvA',
                                '^A<<^A>>^AvvvA',
                                '^<<A^^A>vvvA>A']
    Dictionary_input = [[{'^^^<<A': 1, '>A': 2, 'vvvA': 1}],
             [{'^^^A': 1, 'vA': 1, '<^A': 1, 'vvv>A': 1},
             {'^^^A': 1, 'vA': 1, '^<A': 1, 'vvv>A': 1},
             {'^^^A': 1, 'vA': 1, '<^A': 1, '>vvvA': 1},
             {'^^^A': 1, 'vA': 1, '^<A': 1, '>vvvA': 1}],
             [{'<^A': 1, '^^A': 1, 'v>A': 1, 'vvA': 1},
             {'^<A': 1, '^^A': 1, 'v>A': 1, 'vvA': 1},
             {'<^A': 1, '^^A': 1, '>vA': 1, 'vvA': 1},
             {'^<A': 1, '^^A': 1, '>vA': 1, 'vvA': 1}],
             [{'^A': 1, '<<^A': 1, '>>^A': 1, 'vvvA': 1},
             {'^A': 1, '^<<A': 1, '>>^A': 1, 'vvvA': 1},
             {'^A': 1, '<<^A': 1, '^>>A': 1, 'vvvA': 1},
             {'^A': 1, '^<<A': 1, '^>>A': 1, 'vvvA': 1}],
             [{'^<<A': 1, '^^A': 1, '>vvvA': 1, '>A': 1},
             {'<^<A': 1, '^^A': 1, '>vvvA': 1, '>A': 1},
             {'^<<A': 1, '^^A': 1, 'vv>vA': 1, '>A': 1},
             {'<^<A': 1, '^^A': 1, 'vv>vA': 1, '>A': 1}]]
  
    tot = 0
    for i in range(len(Dictionary_input)):
        s_all = Dictionary_input[i]
        n_all = []
        for s in s_all:
            for j in range(star):
                s = movement_optimized(s)
            n = 0
            for k in list(s.keys()):
                n += len(k)*s[k]
            n_all.append(n)
        print(n_all)
        tot += Input[i]*min(n_all)
    print(tot)

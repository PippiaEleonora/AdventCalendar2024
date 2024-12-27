
import os
import re
import math
import numpy as np
from tqdm import tqdm

def isClique(Clique, Matrix, Nodes, dim):
    Index_list = [Nodes.index(c) for c in Clique]
    M = Matrix[Index_list,:]
    M = M[:,Index_list]
    if np.sum(M) == dim*dim:
        return 1
    else:
        return 0

def find_clique(Nodes, Adj, Matrix, dim):
    max_clique = 0
    for n in tqdm(Nodes):
        for m in Adj[n]:
            Clique = set(Adj[n])
            Clique.add(n)
            Clique = Clique - set([m])
            result = isClique(Clique, Matrix, Nodes, dim)
            if result:
                C = list(Clique)
                C.sort()
                print(C)

if __name__ == '__main__':
    with open('Input23.txt') as f:
        arrayRaw = f.readlines()
        
Adj_dict = {}
for l in arrayRaw:
    l = l.replace('\n','').split('-')
    if l[0] in Adj_dict.keys():
        if not l[1] in Adj_dict[l[0]]:
            Adj_dict[l[0]].append(l[1])
            if l[1] in Adj_dict.keys():
                Adj_dict[l[1]].append(l[0])
            else:
                Adj_dict.update({l[1]: [l[0]]})
    else:
        Adj_dict.update({l[0]: [l[1]]})
        if l[1] in Adj_dict.keys():
            Adj_dict[l[1]].append(l[0])
        else:
            Adj_dict.update({l[1]: [l[0]]})
# First star
Triangles = []
for node in list(Adj_dict.keys()):
    if node[0] == 't':
        for i in range(len(Adj_dict[node])):
            for j in range(i+1,len(Adj_dict[node])):
                n1 = Adj_dict[node][i]
                n2 = Adj_dict[node][j]
                if n2 in Adj_dict[n1]:
                    t = [node,n1,n2]
                    t.sort()
                    if not t in Triangles:
                        Triangles.append(t)
print(len(Triangles))

#Second star
Nodes = list(Adj_dict.keys())
print(len(Nodes))
len_adj = [len(Adj_dict[n]) for n in Nodes]
print(max(len_adj))

Matrix = np.zeros([len(Nodes), len(Nodes)])
for i in range(len(Nodes)):
    Matrix[i,i] = 1
    for j in range(i+1,len(Nodes)):
        if Nodes[j] in Adj_dict[Nodes[i]]:
            Matrix[i,j] = 1
            Matrix[j,i] = 1
find_clique(Nodes,Adj_dict,Matrix,max(len_adj))







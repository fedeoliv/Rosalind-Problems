# http://rosalind.info/problems/gcon/

from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62

def get_score(s, t):
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    f, g, h = {}, {}, {}
    
    m.update({((i, 0), (-5, (i - 1, 0))) for i in range(1, sl + 1)})
    m.update({((0, i), (-5, (0, i - 1))) for i in range(1, tl + 1)})
    
    for i, j in product(range(1, sl + 1), range(1, tl + 1)):
        cost = blosum62.get((s[i - 1], t[j - 1]))
        
        if cost == None:
            cost = blosum62.get((t[j - 1], s[i - 1]))
        f[(i, j)] = m[(i - 1, j - 1)][0] + cost
        g[(i, j)] = max(m[(i - 1, j)][0] - 5, g.get((i - 1, j)))
        h[(i, j)] = max(m[(i, j - 1)][0] - 5, h.get((i, j - 1)))
        v = max(f[(i, j)], g[(i, j)], h[(i, j)])
        if v == f[(i, j)]:
            m[(i, j)] = (v, (i-1, j - 1))
        elif v == g[(i, j)]:
            m[(i, j)] = (v, (i - 1, j))
        elif v == h[(i, j)]:
            m[(i, j)] = (v, (i, j - 1))
    return m[(i,j)][0]
    
if __name__ == '__main__':
    dataset = open('rosalind_gcon.txt').read().strip().split('\n')

    print get_score(dataset[1], dataset[3])

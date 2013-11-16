# http://rosalind.info/problems/edit/

from itertools import product

if __name__ == '__main__':
    distance = {}
    s = 'PLEASANTLY'
    t = 'MEANLY'
    
    distance.update({((i, 0), i) for i in range(len(s) + 1)})
    distance.update({((0, i), i) for i in range(len(t) + 1)})
    
    for i, j in product(range(1, len(s) + 1), range(1, len(t) + 1)):
        if s[i - 1] == t[j - 1]:
            cost = 0
        else:
            cost = 1
            
        distance[(i, j)] = min(distance[(i - 1, j - 1)] + cost, 
                               distance[(i - 1, j)] + 1, distance[(i, j - 1)] + 1)
    
    print distance[(i, j)]

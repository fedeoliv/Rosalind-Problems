# http://rosalind.info/problems/conv/

from collections import Counter
from decimal import Decimal

def get_largest_multiplicity(s1, s2):
    c = Counter()
    
    for i in s1:
        for j in s2:
            c[i - j] += 1
    
    # Getting the most common difference between s1 and s2        
    multiplicity, value = c.most_common(1)[0]
    
    print(value)
    print(abs(multiplicity))
    
if __name__ == '__main__':
    lines = open('rosalind_conv.txt').read().strip().split('\n')
    s1 = [Decimal(x) for x in lines[0].split()]
    s2 = [Decimal(x) for x in lines[1].split()]
    
    get_largest_multiplicity(s1, s2)
    

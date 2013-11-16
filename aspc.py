# http://rosalind.info/problems/aspc/

import math

MODULO = 1000000

def get_prob(m, k):
        return math.factorial(m) / (math.factorial(k) * math.factorial(m - k))

if __name__ == '__main__':
    m = 6
    n = 3
    subsets = 0
    
    for k in range(n, m + 1):
            subsets += get_prob(m, k)

    print subsets % MODULO

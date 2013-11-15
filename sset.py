# http://rosalind.info/problems/sset/

import math

MODULO = 1000000

def get_prob(n, i):
        return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

if __name__ == '__main__':
    n = 824
    subsets = 1
    
    for i in range(1, n + 1):
            subsets += get_prob(n, i)

    print subsets % MODULO

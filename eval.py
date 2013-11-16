# http://rosalind.info/problems/eval/

from collections import Counter
from numpy import log, exp

if __name__ == '__main__':
    lines = open('rosalind_eval.txt').read().strip().split('\n')
    
    n = int(lines[0])
    s = lines[1]
    collection = [float(x) for x in lines[2].split()]
    c = Counter(s)
    
    for number in collection:
        log_p = (c['A'] + c['T']) * log((1 - number) / 2) + (c['C'] + c['G']) * log(number / 2)
        print str(exp(log_p) * (n - 1))

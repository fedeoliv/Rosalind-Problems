# http://rosalind.info/problems/1d/

import re
from itertools import product

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data

def possible_kmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]

def is_valid_kmer(genome,kmer,t): 
    if genome.count(kmer) < t:
        return False
    
    return True

def get_filter_kmer(genome,k,t):
    raw_kmers = possible_kmers(k)
    return set(kmer for kmer in raw_kmers if is_valid_kmer(genome, kmer, t) == True)
    
def get_kmer_position(genome, kmer, k, l, t):
    positions = [m.start() for m in re.finditer(kmer, genome)]
    
    if(positions[t-1] - positions[0] < l):
        return True
    
    return False

def get_distinct_kmers(genome, k, l, t):
    fil_kmers = get_filter_kmer(genome, k, t)
    
    return set(kmer for kmer in fil_kmers if get_kmer_position(genome, kmer, k, l, t) == True)

if __name__ == '__main__':
    genome, n  = [item.strip() for item in read_file('rosalind_1d.txt')]
    k, l, t = [int(item.strip()) for item in n.split(' ')]

    print ' '.join(map(str, get_distinct_kmers(genome, k, l, t)))

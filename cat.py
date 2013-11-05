# http://rosalind.info/problems/cat/

import numpy

MODULO = 1000000L

def get_basepair_edges(i, j):
    if memos[i, j] != -1:
        return memos[i, j]

    result = 0L

    # Verifying if the numbers of bases are right
    rna_substr = rna[i: j + 1]
    
    if rna_substr.count('A') == rna_substr.count('U') and rna_substr.count('C') == rna_substr.count('G'):
        if i > j:
            result = 1L
        elif j == i + 1 and matches[rna[i]] == rna[j]:
            result = 1L
        else:
            result = sum([(get_basepair_edges(i + 1, k - 1) * get_basepair_edges(k + 1, j)) 
                          % MODULO for k in range(i + 1, j + 1, 2) 
                          if matches[rna[i]] == rna[k]]) % MODULO

    memos[i, j] = result
    return result

if __name__ == "__main__":
    with open('rosalind_cat.txt', 'r') as f:
        lines = f.readlines()
        
    # Getting the rna string
    rna = ''.join([line.strip() for line in lines[1:]])
    
    # Creating an array with the length of rna string + 1,
    # initializing each element with random values.
    memos = numpy.empty((len(rna) + 1, len(rna) + 1), dtype = type(0L))
    
    # Filling each element with -1. 
    # In other words, we are replacing the random value by -1.
    memos.fill(-1)
    
    matches = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

    print get_basepair_edges(0, len(rna) - 1)

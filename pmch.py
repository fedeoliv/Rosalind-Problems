# http://rosalind.info/problems/pmch/

from math import factorial

def read_fasta(collection_fasta):
    seq = ""
    
    for line in collection_fasta:
        line = line.rstrip()
        
        if line.startswith(">") == False:
            seq += line
    yield seq

def get_perfect_matchings(rna):
    return factorial(rna.count("A")) * factorial(rna.count("C"))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('rosalind_pmch.txt') as fp:
        for line in read_fasta(fp):
            print get_perfect_matchings(line)

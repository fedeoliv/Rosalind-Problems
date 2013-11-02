# http://rosalind.info/problems/kmer/

from itertools import product

TYPE_MER = 4

def result(dna_str):
    result = []
    
    # Splitting the identifier and the dna string
    dna = parse_fasta(dna_str)
    
    # dna[0][1] will get the dna string
    composition = get_composition(dna[0][1], TYPE_MER)

    
    for kmer in sorted(composition.iterkeys()):
        result.append(composition[kmer])
        
    return result


def parse_fasta(fasta):
    results = []
    strings = fasta.strip().split('>')

    for s in strings:
        if len(s):
            parts = s.split()
            k = parts[0]
            v = ''.join(parts[1:])
            results.append((k, v))

    return results

def possible_kmers(k):
    # Returns all possible strings using 'ATGC'.
    return [''.join(x) for x in product('ATGC', repeat = k)]

def get_composition(s, k):
    kmers = {}
    
    for kmer in possible_kmers(k):
        kmers[kmer] = 0

    for i in range(len(s) - (k - 1)):
        kmer = s[i: i + k]
        kmers[kmer] += 1

    return kmers

if __name__ == "__main__":
    dna_str = open('rosalind_kmer.txt').read().strip()

    print ' '.join(map(str, result(dna_str)))

# http://rosalind.info/problems/1h/

import regex
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from itertools import combinations, product

def get_reverse_complement(text):
    dna = Seq(text, generic_dna)
    return str(dna.reverse_complement())

def get_mismatches(s, d):
    for indices in combinations(range(len(s)), d):
        for replacements in product('ACGT', repeat = d):
            skip = False
            
            for i, a in zip(indices, replacements):
                if list(s)[i] == a:
                    skip = True
            
            if skip:
                continue
            
            key = dict(zip(indices,replacements))
            
            yield ''.join([list(s)[i] if i not in indices else key[i] for i in range(len(s))])

def get_possible_kmers(text, k, d):
    possibles = set()
    correct = set(text[i: i + k] for i in range(len(text) - k + 1))
    i = 1
    
    while i <= d: 
        for s in correct:
            for item in get_mismatches(s, i):
                possibles.add(item)
        i += 1
    return possibles

def get_pairs(seq,k,d):
    possibles = get_possible_kmers(seq,k,d)
    pairs = set()
    
    for kmer in possibles:
        rc_kmer = get_reverse_complement(kmer)
        
        if (kmer,rc_kmer) not in pairs and (rc_kmer,kmer) not in pairs:
            pairs.add((kmer, get_reverse_complement(kmer)))
    
    return pairs

def find_kmer(seq,kmer,d):
    return len(regex.findall(r'(?=(%s){s,e<=%d})'%(kmer,d),seq))

def kmer_composition(seq,k,d):
    all_pair_kmers = get_pairs(seq,k,d)
    composition = {}
    
    for pair_kmers in all_pair_kmers:
        composition[pair_kmers] = sum([find_kmer(seq,i,d) for i in pair_kmers])
    return composition

if __name__ == '__main__':
    dataset = open('rosalind_1g.txt').readlines()
    
    text = dataset[0].strip()
    k, d = (int(x) for x in dataset[1].split(' '))
    
    all_kmers = kmer_composition(text,k,d)
    maximum = max([value for value in all_kmers.itervalues()])
    kmers = [' '.join(key) for key in all_kmers.iterkeys() if all_kmers[key] == maximum]

    print ' '.join(map(str, kmers))

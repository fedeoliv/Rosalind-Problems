# http://rosalind.info/problems/1g/

from itertools import combinations, product
from regex import findall

def get_correct_kmers(text, k):
    correct = set(text[i: i + k] for i in range(len(text) - k + 1))
    return correct

def get_kmers(s, d):
    letters = 'ACGT'
    pool = list(s)
    
    for indices in combinations(range(len(s)),d):
        for replacements in product(letters, repeat = d):
            skip = False
            
            for i, a in zip(indices, replacements):
                if pool[i] == a:
                    skip = True
            
            if skip:
                continue
            
            key = dict(zip(indices,replacements))
            yield ''.join([pool[i] if i not in indices else key[i] for i in range(len(s))])

def all_possible_kmers(text, k, d):
    possibles = set()
    correct = get_correct_kmers(text, k)
    i = 1
    
    while i <= d:
        for s in correct:
            for item in get_kmers(s, i):
                possibles.add(item)
        i += 1
    return possibles

def get_possible_kmers(text, k, d):
    possibles = all_possible_kmers(text, k, d)
    kmers = {}
    
    for kmer in possibles:
        f = findall(r'(?=(%s){s,e<=%d})' % (kmer, d), text)
        kmers[kmer] = len(f)
    
    return kmers

if __name__ == '__main__':
    dataset = open('rosalind_1g.txt').readlines()
    
    text = dataset[0].strip()
    k, d = (int(x) for x in dataset[1].split(' '))
    
    possible_kmers = get_possible_kmers(text, k, d)
    maximum = max([value for value in possible_kmers.itervalues()])
    frequent_kmers = [key for key in possible_kmers.iterkeys() if possible_kmers[key] == maximum]
    
    print(' '.join(map(str, frequent_kmers)))

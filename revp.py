# http://rosalind.info/problems/revp/

from string import maketrans

def reverse_complement(dna):
    return dna[::-1].translate(maketrans('ATCG', 'TAGC'))


def problem(dna):
    # Splitting the dna string in 8 parts
    for i in range(4, 13):
        for j in range(len(dna) - i + 1):
            if dna[j:j+i] == reverse_complement(dna[j: j + i]):
                yield j, dna[j: j + i]


def get_result(result):
    for i, dna in sorted(result):
        print i + 1, len(dna)

def read_fasta(collection_fasta):
    seq = ""
    
    for line in collection_fasta:
        line = line.rstrip()
        
        if line.startswith(">") == False:
            seq += line
    yield seq

if __name__ == '__main__':
    with open('rosalind_revp.txt') as fp:
        for line in read_fasta(fp):
            get_result(problem(line))

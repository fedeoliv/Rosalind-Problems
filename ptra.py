# http://rosalind.info/problems/ptra/

from Bio.Seq import translate

# List of all possible NCBI table codes
NCBI_LIST = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

def translate_dna(dna, ncbi):
    return translate(dna, stop_symbol = "", table = ncbi)

def translate_index(dna, protein):
    for i in NCBI_LIST:
        if translate_dna(dna, i) == protein:
            return i

if __name__ == '__main__':
    dna, protein = open('rosalind_ptra.txt').read().strip().split('\n')
    print translate_index(dna, protein)

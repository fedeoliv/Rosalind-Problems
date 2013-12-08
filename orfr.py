# http://rosalind.info/problems/orfr/

import re
from Bio.Seq import reverse_complement

DNA_CODON = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}

def translate_codon(codon):
    protein = None
    
    if len(codon) == 3 and DNA_CODON.has_key(codon):
        protein = DNA_CODON[codon]
        
    return protein

# generate sub_seqs according to start codons
def refine_start_codon(DNA):
    start_codon_indexes = [m.start() for m in re.finditer('(?=ATG)', DNA)]
    refine_seqs = []
    
    for i in start_codon_indexes:
        refine_seqs.append(re.findall('...',DNA[i:]))
    
    return refine_seqs

# Translating DNA to protein
def translate_dna_protein(seq):
    proteins = []
    
    for sub_seq in refine_start_codon(seq):
        protein = ""
        found_stop = False
        
        for codon in sub_seq:
            if translate_codon(codon) == "Stop":
                found_stop = True
                break
            else:
                protein += translate_codon(codon)
        
        if found_stop:
            proteins.append(protein)
    
    return proteins

if __name__ == '__main__':
    dna = open('rosalind_orfr.txt').readline().strip()
    reversed_dna = reverse_complement(dna)
    
    possibility_dna = translate_dna_protein(dna)
    possibility_rev = translate_dna_protein(reversed_dna)
    
    print max(set(possibility_dna + possibility_rev), key = len)

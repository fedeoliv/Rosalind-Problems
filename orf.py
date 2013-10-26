# http://rosalind.info/problems/orf/

# Creating a constant variable responsible for stop codon in protein translation
STOP_CODON = 'Stop'

# Creating a codon and replacing 'U' by 'T'
codon_table = {
    'TTT': 'F',         'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',         'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',         'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',         'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',         'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',         'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': STOP_CODON,  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': STOP_CODON,  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',         'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': STOP_CODON,  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def revert_translate(dna):
    map_translation = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([map_translation[c] for c in reversed(dna)])

def translate_orf(dna_str):
    results = []
    indices = []
    l = len(dna_str)
    
    for i in range(l):
        # Splitting the dna_str always in 3 parts
        protein = translate_codon(dna_str[i: i + 3])
        
        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        stop_location = False
        protein_str = ''

        for j in range(i, l, 3):
            protein = translate_codon(dna_str[j:j+3])

            if not protein:
                break

            if protein == STOP_CODON:
                stop_location = True
                break

            protein_str += protein

        if stop_location:
            results.append(protein_str)

    return results

def translate_codon(codon):
    protein = None
    
    if len(codon) == 3 and codon_table.has_key(codon):
        protein = codon_table[codon]
    
    return protein

def read_fasta(collection_fasta):
    seq = ""
    
    for line in collection_fasta:
        line = line.rstrip()
        
        if line.startswith(">") == False:
            seq = line
    yield seq
         
if __name__ == "__main__":
    with open('rosalind_orf.txt') as fp:
        for line in read_fasta(fp):
            start_end = translate_orf(line)
            end_start = translate_orf(revert_translate(line))
            
            print "\n".join(set(start_end + end_start))

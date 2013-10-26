# Creating a constant variable responsible for stop codon in protein translation
STOP_CODON = 'Stop'

# Creating a codon map with the respectives keys
codon_table = {
    'UUU': 'F',         'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',         'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',         'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',         'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',         'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',         'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': STOP_CODON,  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': STOP_CODON,  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',         'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': STOP_CODON,  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def codon_frequencies():
    frequencies = {}
    
    # x = key; y = value
    for x, y in codon_table.iteritems():
        if not frequencies.has_key(y):
            frequencies[y] = 0
        
        frequencies[y] += 1
        
    return frequencies


def getTotalRNA(protein_str):
    f = codon_frequencies()
    total = f[STOP_CODON]

    for c in protein_str:
        total *= f[c]

    return total

if __name__ == "__main__":
    print getTotalRNA("MA") % 1000000

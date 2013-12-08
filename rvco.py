# http://rosalind.info/problems/rvco/

from Bio import SeqIO

def get_reverse_comp(dna):
    i = 0
    dna_collection = SeqIO.parse(dna, "fasta")

    for record in dna_collection:
        if str(record.seq) == str(record.seq.reverse_complement()):
            i += 1

    return i

if __name__ == '__main__':
    print get_reverse_comp("rosalind_rvco.txt")

# http://rosalind.info/problems/refs/

from Bio import Entrez

if __name__ == '__main__':
    species, a, b, date = open('rosalind_refs.txt').read().strip().split('\n')
    
    Entrez.email = 'test@example.com'
    terminology = ('srcdb_refseq[Properties] AND {}[Organism] AND {}:{}[Sequence Length] '
            'AND 0:{}[Publication Date]'.format(species, a, b, date))
    nucleotides = Entrez.read(Entrez.esearch(db='nucleotide', term = terminology))
    
    print nucleotides['Count']

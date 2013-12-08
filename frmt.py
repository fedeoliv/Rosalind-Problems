# http://rosalind.info/problems/frmt/

from Bio import SeqIO, Entrez

if __name__ == '__main__':
    collection_id = open('rosalind_frmt.txt').read().strip().split()
    Entrez.email = 'name@server.com'
    
    # Searching for nucleotides into NCBI
    nucleotides = SeqIO.parse(Entrez.efetch(db = 'nucleotide', id = collection_id, rettype = 'fasta'), 'fasta')
    
    print min(nucleotides, key = lambda x: len(x.seq)).format('fasta')

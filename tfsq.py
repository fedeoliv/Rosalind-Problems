# http://rosalind.info/problems/tfsq/

from StringIO import StringIO
from Bio import SeqIO

if __name__ == "__main__":
    with open('rosalind_tfsq.txt') as f:
        records = StringIO("")
        
        # Converting FASTQ to FASTA format.
        SeqIO.convert(f, 'fastq', records, "fasta")
       
        print records.getvalue()

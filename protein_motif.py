# http://rosalind.info/problems/mprt/

import re
from StringIO import StringIO
from Bio import SeqIO
import requests

if __name__ == '__main__':
    file_id = open('rosalind_mprt.txt','r')
    collection_proteins = file_id.read().strip().split('\n')
    
    for protein in collection_proteins:
        # Finding the protein information
        r = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % protein)
        
        # SeqIO is responsible to separate correctly the information in fasta format
        s = SeqIO.read(StringIO(r.text), 'fasta')
        locations = [x for x in re.finditer(r'(?=(N[^P][ST][^P]))',  str(s.seq))]
        
        # Verifying if we have any information about the protein.
        # If we don't have fasta information, we ignore and go to the next step of the loop
        if not len(locations):
            continue
        
        print(protein)
        
        # Joining our list of locations
        print(' '.join([str(l.start(0) + 1) for l in locations]))

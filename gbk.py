from Bio import Entrez

# GenBank is part of the NCBI (National Center for Biotechnology Information).
# So, we will access this bank using the Entrez package, by Bio library.

# For more information: http://biopython.org/DIST/docs/api/Bio.Entrez-module.html

if __name__ == '__main__':
    genus, start, end = open('rosalind_gbk.txt').read().strip().split('\n')
    
    # To make use of NCBI's E-utilities, 
    # NCBI strongly recommends you to specify your email address with each request.
    Entrez.email = 'test@example.com'
    
    # Specific terminology that we need to use to access the data
    terminology = Entrez.esearch(db="nucleotide", term=genus + '[Organism] AND ("' + start + '"[PDAT] : "' + end + '"[PDAT])')
    
    # Searching for the nucleotide ID
    nucleotides = Entrez.read(terminology)

    print nucleotides['Count']

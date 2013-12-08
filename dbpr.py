# http://rosalind.info/problems/dbpr/

from Bio import ExPASy, SwissProt

if __name__ == '__main__':
    # Getting the UniProd ID of a protein
    uniprot_id = SwissProt.read(ExPASy.get_sprot_raw(open('rosalind_dbpr.txt').read().strip()))
    
    # Getting a list of biological processes
    processes = [r[2].split(':')[1] for r in uniprot_id.cross_references 
           if r[0] == 'GO' and r[2].startswith('P')]
    
    print('\n'.join(processes))

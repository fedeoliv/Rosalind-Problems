# http://rosalind.info/problems/nkew/

from StringIO import StringIO
from Bio import Phylo

NEWICK = 'newick'

if __name__ == '__main__':
    results = []
    
    # Splitting the pairs and their respective weights
    pairs = [l2.split('\n') for l2 in open('rosalind_nkew.txt').read().strip().split('\n\n')]
    
    for s, animals in pairs:
        # Splitting the animals that we will use for weight comparison
        x, y = animals.split()
        
        # Phylo.read is a function responsible to get all the information about the collection
        tree = Phylo.read(StringIO(s), NEWICK)
        
        # tree.distance will sum all the weights.
        # In this case, we want just the integer value.
        results.append(int(tree.distance(x, y)))
        
    print(" ".join(str(x) for x in results))

from StringIO import StringIO
from Bio import Phylo

if __name__ == '__main__':
    distances = []
    
    # Splitting the pairs
    pairs = [line.split('\n') for line in open('rosalind_nwck.txt').read().strip().split('\n\n')]
    
    for s, line2 in pairs:
        x, y = line2.split()
        
        # This function in Bio library is responsible to get several information
        # about differences between pairs. In this case, we want the distance between them.
        tree = Phylo.read(StringIO(s), 'newick')
        
        distances.append(int(tree.distance(x, y)))
        
    print ' '.join(map(str, distances))

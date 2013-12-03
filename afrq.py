# http://rosalind.info/problems/afrq/

from numpy import roots

if __name__ == '__main__':
    probabilities = []
    
    # Splitting the proportion in an array
    proportion_recessives = [float(x) for x in open('rosalind_afrq.txt').read().strip().split()]
    
    for prop in proportion_recessives:
        q = prop ** 0.5
        
        # Getting the max value between the 'k-mer' root and the root related to uniform alleles
        p = max(roots([1, 2 * q, q ** 2 - 1]))
        probabilities.append((2 * p * q) + (q ** 2))
    
    print(" ".join(str(x) for x in probabilities))

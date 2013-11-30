from numpy import log10, asarray, exp, where

# Same function used in the open source scipy library.
def comb(N,k,exact=0):
    if exact:
        if (k > N) or (N < 0) or (k < 0):
            return 0
        val = 1
        
        for j in xrange(min(k, N-k)):
            val = (val*(N-j))//(j+1)
            
        return val
    else:
        from scipy import special
        
        k,N = asarray(k), asarray(N)
        lgam = special.gammaln
        
        cond = (k <= N) & (N >= 0) & (k >= 0)
        sv = special.errprint(0)
        vals = exp(lgam(N+1) - lgam(N-k+1) - lgam(k+1))
        sv = special.errprint(sv)
        
        return where(cond, vals, 0.0)

if __name__ == '__main__':
    n = int(open('rosalind_indc.txt').read().strip())
    
    # Calculating the common algorithm of the probability
    common_alg = [log10(comb(2 * n, i)) + i * log10(0.5) + (2 * n - i) * log10(0.5) for i in range(n * 2 + 1)]
    prob = [10 ** x for x in common_alg]
    probabilities = [0 for _ in prob]
    
    for i in range(n*2, -1, -1):
        probabilities[i] = log10(sum([prob[j] for j in range(i, n*2 + 1)]))
        
    print(' '.join([str(x) for x in probabilities[1:]]))

# http://rosalind.info/problems/foun/ 

from math import log

def fac(n):
    r = 1

    while n != 0:
        r *= n
        n -= 1

    return r

def C(n,k):
    return int(fac(n) / (fac(n - k) * fac(k)))

def Bin(N,k,p):
    return C(N, k) * p**k * (1 - p) ** (N - k)

def dist(N, i0, g):
    P = [0.0 for _ in range(2 * N + 1)]
    P[i0] = 1.0

    for _ in range(g):
        nP = [0.0 for _ in range(2 * N + 1)]
       
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                nP[i] += P[j] * Bin(2 * N, i, j / float(2 * N))
        P = nP
    
    return P

if __name__ == '__main__':
    with open('rosalind_foun.txt') as f:
        line = f.readline()
        line = line.strip()
        N,m = [int(x) for x in line.split()]
        line = f.readline()
        line = line.strip()
        A = [int(x) for x in line.split()]
        k = len(A)
    
    mat = [[0.0 for _ in range(k)] for _ in range(m)]

    for i in range(k):
        for j in range(m):
            mat[j][i] = dist(N, 2 * N - A[i], j + 1)[2 * N]
    
    print("\n".join([" ".join([str(log(x,10)) for x in row]) for row in mat]))

# http://rosalind.info/problems/root/

MODULO = 1000000

def get_count_leaves(n, i):
    if i + i == n:
        return c[n][i] / 2
    else:
        return c[n][i]

def get_b(n):
    for i in xrange(n + 1):
        for j in xrange(i + 1):
            if j == 0 or i == j:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % 10 ** 7
    
    for i in xrange(2, n + 1):
        t.append(0)
        
        for fp in xrange(1, i / 2 + 1):
            t[i] = (t[i] + t[fp] * t[i - fp] * get_count_leaves(i, fp)) % 10 ** 6
    return t[n]

if __name__ == "__main__":
    n = 4
    t = [0, 1]
    c = map(list, [[0] * (n + 1)] * (n + 1))
    
    print get_b(n) % MODULO

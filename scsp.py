def lcs(s, t):
    lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i+1][j], lengths[i][j+1])
    
    # Reading the substring out of the matrix
    result = ""
    x, y = len(s), len(t)
    
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            assert s[x - 1] == t[y - 1]
            result = s[x - 1] + result
            x -= 1
            y -= 1
    return result

def get_supersequence(s, t):
    subsequence = lcs(s, t)
    supersequence = ""
    i, j = 0, 0
    
    for c in subsequence:
        if i < len(s):
            while s[i] != c:
                supersequence += s[i]
                i += 1
            i += 1
        if j < len(t):
            while t[j] != c:
                supersequence += t[j]
                j += 1
            j += 1
        supersequence += c
    if i < len(s):
        supersequence += s[i:]
    if j < len(t):
        supersequence += t[j:]
    return supersequence

if __name__ == '__main__':
    dataset = open('rosalind_scsp.txt').readlines()
    
    s, t = [line.strip() for line in dataset]
    print get_supersequence(s, t)

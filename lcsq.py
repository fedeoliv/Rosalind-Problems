# http://rosalind.info/problems/lcsq/

import itertools
    
def lcs(s, t):
    s_length, t_length = len(s), len(t)
    
    if s_length == 0:
        return []
    elif s_length == 1:
        if s[0] in t:
            return [s[0]]
        else:
            return []
    else:
        i = s_length // 2
        s_beginning, s_end = s[:i], s[i:]
        
        ll_b = lcs_length(s_beginning, t)
        ll_e = lcs_length(s_end[::-1], t[::-1])
        _, k = max((ll_b[j] + ll_e[t_length - j], j) for j in range(t_length + 1))
        
        t_beginning, t_end = t[:k], t[k:]
        
        return lcs(s_beginning, t_beginning) + lcs(s_end, t_end)
    
def lcs_length(s, t):
    current = list(itertools.repeat(0, 1 + len(t)))
    
    for x in s:
        prev = list(current)
        
        for i, y in enumerate(t):
            if x == y:
                current[i + 1] = prev[i] + 1
            else:
                current[i + 1] = max(current[i], prev[i + 1])
    return current

if __name__ == '__main__':
    print ''.join(lcs("AACCTTGG", "ACACTGTGA"))

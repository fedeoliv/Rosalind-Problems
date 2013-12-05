# http://rosalind.info/problems/rnas/

def get_sum_matchings(s):
    x = map(list, [[0] * len(s)] * len(s))
    
    # Allowed edges are used for comparison
    allowed_edges = frozenset(map(frozenset, ('AU', 'CG', 'GU')))
    
    for ln in xrange(1, len(s) + 1):
        for start in xrange(0, len(s) - ln + 1):
            end = start + ln - 1
            
            if ln <= 4:
                x[start][end] = 1
            else:
                x[start][end] = x[start + 1][end]
                
                for conn in xrange(start + 4, end + 1):
                    if frozenset((s[start], s[conn])) in allowed_edges:
                        temp = x[start + 1][conn - 1] * ((x[conn + 1][end] if conn != end else 1))
                        x[start][end] += temp
                        
    return x[0][len(s) - 1]

if __name__ == '__main__':
    with open('rosalind_rnas.txt') as f:
        s = f.readline().strip()
    
    print get_sum_matchings(s)

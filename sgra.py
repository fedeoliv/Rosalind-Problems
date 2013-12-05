# http://rosalind.info/problems/sgra/

MONOISOTOPIC_TABLE = list((('A', 71.03711),  ('C', 103.00919), ('D', 115.02694),
                           ('E', 129.04259), ('F', 147.06841), ('G', 57.02146),
                           ('H', 137.05891), ('I', 113.08406), ('K', 128.09496),
                           ('L', 113.08406), ('M', 131.04049), ('N', 114.04293),
                           ('P', 97.05276),  ('Q', 128.05858), ('R', 156.10111),
                           ('S', 87.03203),  ('T', 101.04768), ('V', 99.06841),
                           ('W', 186.07931), ('Y', 163.06333),))

def get_longest_protein(n):
    answer = [None] * n
    
    for i in xrange(n - 1, -1, -1):
        answer[i] = (0, '')
        
        for j in xrange(i + 1, n):
            node = get_valid_edge(weighted_strings[j] - weighted_strings[i])
            
            if node: 
                rs = answer[j][0] + 1
                
                if rs > answer[i][0]:
                    answer[i] = (rs, node + answer[j][1])
                    
    return ''.join(max(answer)[1])
    
def get_valid_edge(s):
    for (j, k) in MONOISOTOPIC_TABLE:
        if abs(k - s) < 0.01:
            return j
    return None

if __name__ == '__main__':
    weighted_strings = [float(mass) for mass in open('rosalind_sgra.txt').read().strip().split('\n')]
    
    print get_longest_protein(len(weighted_strings))

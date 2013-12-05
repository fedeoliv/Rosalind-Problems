# http://rosalind.info/problems/motz/

MODULO = 1000000L

def get_motzkin_numbers(s):
    if s in noncrossing_matchings:
        return noncrossing_matchings[s]
    else:
        output = 1L
        if len(s) == 2 and match(s[0], s[1]):
            output = 2L
        elif len(s) > 2:
            output = get_motzkin_numbers(s[1:]) + sum([match(s[0], s[k]) * get_motzkin_numbers(s[1: k])
                    * get_motzkin_numbers(s[k + 1:]) for k in range(1, len(s))])

        output %= MODULO
        noncrossing_matchings[s] = output
        
        return output
    
if __name__ == '__main__':
    rna = ''
    noncrossing_matchings = {}
    
    with open('rosalind_motz.txt') as f:
        for line in f:
            if line.startswith('>') == False:
                rna += line
                
    match = lambda s, t: set([s, t]) == set(['A', 'U']) or set([s, t]) == set(['C', 'G'])
    
    print "{}\n".format(get_motzkin_numbers(rna))

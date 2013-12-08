# http://rosalind.info/problems/1c/

import re

if __name__ == '__main__':
    pattern, text = open('rosalind_1c.txt').read().strip().split('\n')
    results = [m.start() for m in re.finditer('(?=%s)'%pattern,text)]
    
    print ' '.join(map(str,results))

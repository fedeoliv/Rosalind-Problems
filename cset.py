# http://rosalind.info/problems/cset/

import chbp

if __name__ == "__main__":
    with open('rosalind_cset.txt') as f:
        chars = f.read()
        chars = chars.strip()
        chars = chars.split()
    
    taxa = [str(n) for n in range(len(chars[0]))]
    for i in range(len(chars)):
        nchars = chars[:i] + chars[i+1:]
        
        # We can have more than one solution, 
        # but the problem explains that we can show any solution.
        if chbp.consistent(nchars,taxa):
            print("\n".join(nchars))
            break

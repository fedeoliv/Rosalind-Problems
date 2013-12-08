# http://rosalind.info/problems/1b/

if __name__ == "__main__":
    dna = open("rosalind_1b.txt").read()
    ans = ""
    
    for i in reversed(range(len(dna))):
        if dna[i] == 'A':
            ans = ans + 'T'
        elif dna[i] == 'T':
            ans = ans + 'A'
        elif dna[i] == 'C':
            ans = ans + 'G'
        elif dna[i] == 'G':
            ans = ans + 'C'
    
    print ans

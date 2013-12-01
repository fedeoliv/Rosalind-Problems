def get_reverse_complement(s):
    ret = ""
    for c in s[::-1]:
        ret += "ATGC"["TACG".find(c)]    
    return ret

if __name__ == '__main__':
    t = [x.strip() for x in open('rosalind_dbru.txt').readlines()]
    f = open('dbru_out.txt','w')
    s = []
    c = {}
    
    for e in t:
        s.append(e)
        s.append(get_reverse_complement(e))
    
    for i in range(len(s)):
        c[s[i][:len(s[i])-1], s[i][1:]] = 1
    
    # If you use Eclipse platform, you need to write the answer into a file, 
    # because the console doesn't support many strings.    
    for e in c:
        f.write(str(e).replace("'", ''))
        f.write('\n')
        
    f.close()

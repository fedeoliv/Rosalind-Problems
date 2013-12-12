# http://rosalind.info/problems/gasm/

ALPHABET = "ATGC"
COMPLEMENT = {"A":"T","T":"A","G":"C","C":"G"}

def rc(dna):
    ret = ""

    for i in range(len(dna)):
        ret = COMPLEMENT[dna[i]] + ret

    return ret

def compute_distance(s1,s2):
    if len(s2) == 0:
        return 0

    pos = 0
    
    while pos != -1:
        l = len(s1) - pos
        if s1[pos:] == s2[:l]:
            return len(s2) - l

        pos = s1.find(s2[0],pos+1)

    return len(s2)

if __name__ == '__main__':
    dnas = [x.strip() for x in open('rosalind_gasm.txt').readlines()]
    
    
    for k in reversed(range(2,len(dnas[0])+1)):
        mers = set()
    
        for s in dnas:
            for i in range(len(s)-k+1):
                mers.add(s[i:i+k])
                mers.add(rc(s[i:i+k]))
    
        ans = None
    
        stack = []
        stack.append(([],set()))
        
        while len(stack) > 0 and ans == None:
            path,vs = stack.pop()
    
            if len(path) == 0:
                for mer in mers:
                    stack.append(([mer],set([mer])))
            else:
                mer = path[-1]
        
                for a in ALPHABET:
                    nmer = mer[1:] + a
                
                    if nmer in mers and nmer != rc(mer):
                        if nmer == path[0]:
                            ans = list(path)
                            break
                        elif not nmer in vs:
                            stack.append((path + [nmer],vs.union(set([nmer]))))
    
        if ans != None:
            output = ans[0]
          
            for i in range(1, len(ans)):
                output += ans[i][-1]
                
            output = output[:-(k-1)]
            doutput = output + output
            success = True
            
            for dna in dnas:
                if doutput.find(dna) == -1 and doutput.find(rc(dna)) == -1:
                    success = False
    
            if success:
                print output
                break

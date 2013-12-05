# http://rosalind.info/problems/qrt/

def get_quartets(k):
    quartets = []
    tmp_final = list()
    final = list()
    
    for item in pct :
        # A and B represent two subsets of a quartet.
        # A contains ones only and B contains zeros only
        a, b = [], []
        
        for i in range(len(item)) :
            if item[i] == '1':
                a.append(i)
            elif item[i] == '0':
                b.append(i)
                
        # Verifying if those are not trivial characters
        if (len(a) > 1) and (len(b) > 1) :
            aa = get_pair_combinations(a)
            bb = get_pair_combinations(b)
            
            for ii in range(len(aa)):
                for jj in range(len(bb)):
                    t = list()
                    t.append(aa[ii])
                    t.append(bb[jj])
                    tmp_final.append(t)
         
    i = 0
    
    while i < len(tmp_final):
        flag = True
        j = i + 1
        
        while j < len(tmp_final):
            if ((len(set(tmp_final[i][0]).difference(tmp_final[j][0])) == 0) 
                and (len(set(tmp_final[i][1]).difference(tmp_final[j][1])) == 0)) \
                or ((len(set(tmp_final[i][0]).difference(tmp_final[j][1])) == 0) \
                and (len(set(tmp_final[i][1]).difference(tmp_final[j][0])) == 0)):
                flag = False
            j += 1
        if flag == True :    
            final.append(tmp_final[i])
        i += 1
    
    for item in final :
        quartets.append('{' + item[0][0] + ', ' + item[0][1] + '}' + ' ' + '{' + item[1][0] + ', ' + item[1][1] + '}')
      
    return quartets

# Getting all possible combinations within A and B
def get_pair_combinations(characters):
    output = list()
    m = 0
    
    while m < len(characters):
        n = m + 1
        while n < len(characters):
            t = list()
            t.append(taxa[characters[m]])
            t.append(taxa[characters[n]])
            output.append(t)
            n += 1
        m += 1
    
    return output

if __name__ == "__main__":
    dataset = open('rosalind_qrt.txt')
    taxa, pct = [], []
    k = 0
    
    while True:
        line = dataset.readline()
        if not line: break
        
        if k == 0: 
            for item in line.strip().split(' '):
                taxa.append(item.strip())
        else: pct.append(line.strip())
        
        k += 1
    
    print "\n".join(str(x) for x in get_quartets(k))
    
        

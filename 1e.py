# http://rosalind.info/problems/1e/

if __name__ == "__main__":
    genome = open("rosalind_1e.txt").read()
    l = []
    count = 0
    l.append(count)
    
    for i in range(len(genome)):
        if genome[i] == 'G':
            count += 1
        elif genome[i] == 'C':
            count -= 1
        
        l.append(count)
    
    min_skew = min(l)
    answer = ''
    
    for i in range(len(l)):
        if l[i] == min_skew:
            answer += ' ' + str(i)   
                 
    print answer.strip()

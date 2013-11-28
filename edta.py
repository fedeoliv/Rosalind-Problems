def get_alignment(s,t):
    matrix = {(i,j): ( j+i+2 , (max(i-1,-1),max(j-1,-1),(s[i] if i>=0 else '-') ,(t[j]) if j>=0 else '-') ) for i in range(-1,len(s)) for j in range(-1,len(t))}
    matrix[-1,-1] = (0,(-1,-1,'',''))

    [gap_symbol(matrix, i, j) for i in range(len(s)) for j in range(len(t))]

    return matrix

def gap_symbol(matrix, i, j):
        i_gap = (matrix[i - 1, j][0] + 1, (i - 1, j, s[i], "-") )
        j_gap = (matrix[i, j - 1][0] + 1, (i, j - 1, "-", t[j]))
        non_gap = (matrix[i - 1, j - 1][0] + int(s[i] != t[j]), (i - 1, j - 1, s[i], t[j]))
        
        matrix[i, j] = min(i_gap, j_gap, non_gap)

def get_output(strings, s, t):
    last = strings[len(s)-1,len(t)-1]
    max_gap = last[0]
    aug_s = [last[1][2]]
    aug_t = [last[1][3]]
    
    while (last[1][2],last[1][3]) != ('',''):
        last = strings[last[1][0],last[1][1]]
        aug_s.append(last[1][2])
        aug_t.append(last[1][3])
    
    return (max_gap, "".join(aug_s[::-1]), "".join(aug_t[::-1]))

if __name__ == "__main__":
    f = open("rosalind_edta.txt")
    s, t = [i.strip() for i in f.readlines()]
    
    strings = get_alignment(s,t)
    distance, aug_s, aug_t = get_output(strings, s, t)
    
    print distance, '\n', aug_s, '\n ', aug_t

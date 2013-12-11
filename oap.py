# http://rosalind.info/problems/oap/

from Bio import SeqIO

def create_empty_matrix(dimensions):
    matrix = []
    
    for _ in range(dimensions[0]):
        matrix.append([])
        
        for _ in range(dimensions[1]):
            matrix[-1].append(0)
    return matrix

#No substitution matrix, just simple linear gap penalty model
def get_match_score(s, t):
    if s == t:
        return match_award
    elif s == '-' or t == '-':
        return gap_penalty
    else:
        return mismatch_penalty
    
def get_score(s, t):
    align_s, align_t = '', ''
    score = create_empty_matrix((len(t) + 1, len(s) + 1))
    pointer = create_empty_matrix((len(t) + 1, len(s) + 1))
    
    for i in range(len(t) + 1):
        score[i][0] = 0
        pointer[i][0] = 1
    
    for j in range(len(s) + 1):
        score[0][j] = 0
        pointer[0][j] = 2
        
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            score_diagonal = score[i - 1][j - 1] + get_match_score(s[j - 1], t[i - 1])
            score_up = score[i][j - 1] + gap_penalty
            score_left = score[i - 1][j] + gap_penalty
            score[i][j] = max(score_left, score_up, score_diagonal)
            
            # 3 = Diagonal trace
            # 2 = Left trace
            # 1 = Up trace
            
            if score[i][j] == score_diagonal :
                pointer[i][j] = 3
            elif score[i][j] == score_up :
                pointer[i][j] = 2
            elif score[i][j] == score_left :
                pointer[i][j] = 1
                
    max_score = -200
    
    for ii in range(len(t) + 1) :
        if score[ii][-1] >= max_score :
            max_score = score[ii][-1]
            i = ii
            
    print max_score
    
    while True: 
        if (pointer[i][j] == 3):
            align_s = s[j - 1] + align_s
            align_t = t[i - 1] + align_t
            i -= 1
            j -= 1
        elif (pointer[i][j] == 2):
            align_t = '-' + align_t
            align_s = s[j - 1] + align_s
            j -= 1
        elif (pointer[i][j] == 1):
            align_t = t[i - 1] + align_t
            align_s = '-' + align_s
            i -= 1
            
        if (i == 0 or j == 0): break
        
    return align_s + '\n' + align_t

if __name__ == "__main__":
    dna_list = list(SeqIO.parse("rosalind_oap.txt", "fasta"))

    s = dna_list[0].seq
    t = dna_list[1].seq
    
    match_award = 1
    mismatch_penalty = -2
    gap_penalty = -2

    print get_score(s, t)

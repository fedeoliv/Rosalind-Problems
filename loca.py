# http://rosalind.info/problems/loca/

def pam250(c1, c2) :
    i = 0
    j = 0
    
    if c1 == 'A' : i = 0
    if c1 == 'R' : i = 1
    if c1 == 'N' : i = 2
    if c1 == 'D' : i = 3
    if c1 == 'C' : i = 4
    if c1 == 'Q' : i = 5
    if c1 == 'E' : i = 6
    if c1 == 'G' : i = 7
    if c1 == 'H' : i = 8
    if c1 == 'I' : i = 9
    if c1 == 'L' : i = 10
    if c1 == 'K' : i = 11
    if c1 == 'M' : i = 12
    if c1 == 'F' : i = 13
    if c1 == 'P' : i = 14
    if c1 == 'S' : i = 15
    if c1 == 'T' : i = 16
    if c1 == 'W' : i = 17
    if c1 == 'Y' : i = 18
    if c1 == 'V' : i = 19
       
    if c2 == 'A' : j = 0
    if c2 == 'R' : j = 1
    if c2 == 'N' : j = 2
    if c2 == 'D' : j = 3
    if c2 == 'C' : j = 4
    if c2 == 'Q' : j = 5 
    if c2 == 'E' : j = 6
    if c2 == 'G' : j = 7
    if c2 == 'H' : j = 8
    if c2 == 'I' : j = 9
    if c2 == 'L' : j = 10
    if c2 == 'K' : j = 11
    if c2 == 'M' : j = 12
    if c2 == 'F' : j = 13
    if c2 == 'P' : j = 14
    if c2 == 'S' : j = 15
    if c2 == 'T' : j = 16
    if c2 == 'W' : j = 17
    if c2 == 'Y' : j = 18
    if c2 == 'V' : j = 19
    
    pam250 = [[2,  -2,  0,  0, -2,  0,  0,  1, -1, -1, -2, -1, -1, -3,  1,  1,  1, -6, -3,  0],
              [-2,  6,  0, -1, -4,  1, -1, -3,  2, -2, -3,  3,  0, -4,  0,  0, -1,  2, -4, -2],
              [0,   0,  2,  2, -4,  1,  1,  0,  2, -2, -3,  1, -2, -3,  0,  1,  0, -4, -2, -2],
              [0,  -1,  2,  4, -5,  2,  3,  1,  1, -2, -4,  0, -3, -6, -1,  0,  0, -7, -4, -2],
              [-2, -4, -4, -5, 12, -5, -5, -3, -3, -2, -6, -5, -5, -4, -3,  0, -2, -8,  0, -2],
              [0,   1,  1,  2, -5,  4,  2, -1,  3, -2, -2,  1, -1, -5,  0, -1, -1, -5, -4, -2],
              [0,  -1,  1,  3, -5,  2,  4,  0,  1, -2, -3,  0, -2, -5, -1,  0,  0, -7, -4, -2],
              [1,  -3,  0,  1, -3, -1,  0,  5, -2, -3, -4, -2, -3, -5,  0,  1,  0, -7, -5, -1],
              [-1,  2,  2,  1, -3,  3,  1, -2,  6, -2, -2,  0, -2, -2,  0, -1, -1, -3,  0, -2],
              [-1, -2, -2, -2, -2, -2, -2, -3, -2,  5,  2, -2,  2,  1, -2, -1,  0, -5, -1,  4],
              [-2, -3, -3, -4, -6, -2, -3, -4, -2,  2,  6, -3,  4,  2, -3, -3, -2, -2, -1,  2],
              [-1,  3,  1,  0, -5,  1,  0, -2,  0, -2, -3,  5,  0, -5, -1,  0,  0, -3, -4, -2],
              [-1,  0, -2, -3, -5, -1, -2, -3, -2,  2,  4,  0,  6,  0, -2, -2, -1, -4, -2,  2],
              [-3, -4, -3, -6, -4, -5, -5, -5, -2,  1,  2, -5,  0,  9, -5, -3, -3,  0,  7, -1],
              [1,   0,  0, -1, -3,  0, -1,  0,  0, -2, -3, -1, -2, -5,  6,  1,  0, -6, -5, -1],
              [1,   0,  1,  0,  0, -1,  0,  1, -1, -1, -3,  0, -2, -3,  1,  2,  1, -2, -3, -1],
              [1,  -1,  0,  0, -2, -1,  0,  0, -1,  0, -2,  0, -1, -3,  0,  1,  3, -5, -3,  0],
              [-6,  2, -4, -7, -8, -5, -7, -7, -3, -5, -2, -3, -4,  0, -6, -2, -5, 17,  0, -6],
              [-3, -4, -2, -4,  0, -4, -4, -5,  0, -1, -1, -4, -2,  7, -5, -3, -3,  0, 10, -2],
              [0,  -2, -2, -2, -2, -2, -2, -1, -2,  4,  2, -2,  2, -1, -1, -1,  0, -6, -2,  4]]
    
    return pam250[i][j]

def zeros(shape):
    retval = []
    for _ in range(shape[0]):
        retval.append([])
        for _ in range(shape[1]):
            retval[-1].append(0)
    return retval

def match_score(alpha, beta):
    if alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return pam250(alpha, beta)

def get_score(align1, align2):
    i, score = 0, 0
    symbol = ''
    global output
    
    for i in range(0,len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:
            symbol = symbol + align1[i]
            score += match_score(align1[i], align2[i])
    
        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-':
            score += match_score(align1[i], align2[i])
            symbol += ' '
    
        #if one of them is a gap, output a space
        elif align1[i] == '-' or align2[i] == '-':
            symbol += ' '
            score += gap_penalty
    
    print score
    print align1.replace("-", "")
    print align2.replace("-", "")
    
def get_alignment_score(seq1, seq2):
    m, n = len(seq1), len(seq2) # length of two sequences
    
    # Generate DP table and traceback path pointer matrix
    score = zeros((m+1, n+1)) # the DP table
    pointer = zeros((m+1, n+1)) # to store the traceback path
    max_score = 0 # initial maximum score in DP table
    
    # Calculate DP table and mark pointers
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_diagonal = score[i-1][j-1] + match_score(seq1[i-1], seq2[j-1])
            score_up = score[i][j-1] + gap_penalty
            score_left = score[i-1][j] + gap_penalty
            score[i][j] = max(0,score_left, score_up, score_diagonal)
            
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3 # 3 means trace diagonal
            if score[i][j] == score_up:
                pointer[i][j] = 2 # 2 means trace left
            if score[i][j] == score_left:
                pointer[i][j] = 1 # 1 means trace up
            if score[i][j] == 0:
                pointer[i][j] = 0 # 0 means end of the path
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j];
                
    align1, align2 = '', ''
    
    i = max_i
    j = max_j
    
    while  pointer[i][j] != 0:
        if pointer[i][j] == 3:
            align1 =  seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            align1 = '-' + align1
            align2 = seq2[j-1] + align2
            j -= 1
        elif pointer[i][j] == 1:
            align1 = seq1[i-1] + align1
            align2 = '-' + align2
            i -= 1
            
    get_score(align1, align2)
    
if __name__ == "__main__":
    s = "NYHMGVVHYDRFNFYGDYYKPWNVRYNHGSDFSETTEYPAFKAKFSIQMQLLCHKSHMKNNPLDHHMWPKKMLKNCPWFFEHPEEEWFLEFDHSNYNECYPEAYCGCEFVDRIRVTQNDRAGCHAPWESIGCNCFGSFTRHTEAAAMHDTMEGCIGWSRDQDFRGCSLQSCIFPEMTLEPEFFNKNYNAKSRRAIMRWRYSYVFPCYVYYGGWGHQYADRESDGGADFVCVCNTCAWIVMLWKHEYYKTYTENYPCGIGLIAFNKNYFMRQNWFHETFEPHVRYFMNIGWLWWLGPNENDFDVNTAEQELFDRPRLTFTEDPMQETVSDTCMCESVWMSLEDYREADHPQTDMMCKYLFGFTFSVLPDQKGLLDCPVHQVRAYIQPLYGYRAGHETYCGCHQSYNLFYAPLGCQMSKGSGYHRKKHVMHIQCLSTNRMETIHKVDEWGFWAGTCHFSPDSEISPDWQGMYKKMESENSGQVKQKRKIYAMFMRHWGPYSKDRPLAAPAYFSCKGLCPDLIQENDNHHYKKPKVDVYWGYTENFISYMQMLGFCCDRIGMHAKATEGPRQRECEKETERQMKDLSMDETHLMMHQNTNPEKIRIPIDLKSRIGWKRPNDEHNKFLYAQVMMKGFEWHMYGGQEEWRQFRNNENSVDTKKLLWVDRYGMEDKRARKLHVITNTGDNGRKCNHAHWGMWPKHCMPWIVYDAPWEWLSIYTAGAAIFWEYYAPSKWVTWHPKWKKSVKYNVSINPAALNQKKNCYLFHPDYTPHCRLINPQGPNMSNWQPFCEHKYWILAQQNMDCQHCFKVSIHHEAKMYPGFCPGWMWDRQVRRPCDSVRVKMEPCAGVYLQSMGQEYITRPTSLSKFVMGIEKYTTTGNNTQQRTSHPTSNYCLNDSVGPH"
    t = "GKVFAEATDYMWVGLSIWGPCNMQAKENETKNKGMFESPQSHHAYSGGLGWVKGCGMHVKHDQRHCVLRCNERYHYVKWHLDERATVVDKQMYSHRWCGLRKNDEIELKFLRMTGKRYCNNFRPKHKWAMVRTEFKYREYEEYPRTNYENSIEPDCSVHVCGMEMWCVILHPMNNADDGGWPETHPANSVNIIYYLKHCDQSDYYTFKPAGKTLTCCNTKVQQENGCHIQHDWRRFPLWLDNFWWTEVFHLIEYLCDHFYYNLTPYDGGMSPCYYHQWGVFQIDTNFEPHVRYESNPMNIGWLWWLGPNFNDFDVNTAEQELFDRPRCVVHDTCNVCDSVYHWLLFEMMSLEDYYEADPPQTDHDLHMCKYLFGFLDNAEIRQCRAYIQPLYGIRAGHEYCGCHQSYNRFYAPLGCHRKKPVMHIQCLSTNRMETIHKSPCIPSTNEWGWDDRWAGTCHFSPDSEISGMYKKFKQESENSGQVKQKRKIFQMWSFCMRPWGPYGFSTLGPLAAPAYSSCKGVDNDNHHKKNKGAIWDDFENFISYMQMIGFNCDRIGKATEGRRQQRHCEKETERVMSDLSLMMLQNLKSRIGWKRKKKFSVKMDEHNKFGGPCYSCVYAQVMMEGESPSEWKLACKIMCNGQEEWCKGGLWSGSRCMMSWSVYNNLIKHTLQKQRLSSAPCGMWMFRYNFFTFTCSWTAKQSPQFPIQDHSAVWKSMEGNTEEDFKSCLGEQKVSDNKIHDTGAIFQCKYSHTVRPSYDQQNFPKIVCDCVKNEEWTVWLWCQRTHHRTNTDDFARPRIRQKWTNYVDWGLNGHWLDGGRHPQKCIIPMQELGIYDVQVEGIWNWWKRACRFWECTHILTIFHFAIEPYSADPAWGQSPKGWRDIRVAVMHYIPQAKASFDDGRDREWSRC"
    match_award = 5
    mismatch_penalty = -5
    gap_penalty = -5 
    
    get_alignment_score(s, t)

# http://rosalind.info/problems/1a/

if __name__ == "__main__":
    seq, k = open('rosalind_1a.txt').read().strip().split('\n')
    
    dictionary = {}
    string_set = set([])
    n_kmar = 0
    ans = []

    for i in range(0, len(seq) - int(k) + 1):
        s = seq[i:i + int(k)]
        
        if (s in string_set):
            dictionary[s] = dictionary[s] + 1
            n_kmar = max(n_kmar, dictionary[s])
        else:
            dictionary[s] = 1;
            string_set.add(s)
            n_kmar = max(n_kmar, dictionary[s])

    for k in dictionary.keys():
        if (dictionary[k] == n_kmar):
            ans.append(k)

    print ' '.join(ans)

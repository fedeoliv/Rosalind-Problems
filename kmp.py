# http://rosalind.info/problems/kmer/

def read_fasta(collection_fasta):
    seq = ""
    
    for line in collection_fasta:
        line = line.rstrip()
        
        if line.startswith(">") == False:
            seq += line
    yield seq
    
def get_failure(s):
    j = -1
    b = [j]

    for _, c in enumerate(s):
        while j >= 0 and s[j] != c:
            j = b[j]
            
        j += 1
        b.append(j)

    return b[1:]


if __name__ == "__main__":
    with open('rosalind_kmp.txt') as fp:
        for line in read_fasta(fp):
            results = get_failure(line)

            # Joining the results and splitting by ' '
            print ' '.join(map(str, results))

# http://rosalind.info/problems/lcsm/

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

def long_substr(data):
    substr = ''
    
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def read_fasta(fp):
    name, seq = None, []
    
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


data_list = []

with open('shared_motif.txt') as fp:
    for name, seq in read_fasta(fp):
        data_list.append(seq)

print long_substr(data_list)

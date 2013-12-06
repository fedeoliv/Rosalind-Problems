# http://rosalind.info/problems/grph/

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
name_list = []

with open('rosalind_graphs.txt') as fp:
    for name, seq in read_fasta(fp):
        data_list.append(seq)
        name_list.append(name)
        
n = len(data_list)

for x in range(n):
    for y in range(n)[x + 1: n]:
            if data_list[x][0:3] == data_list[y][::-1][0:3][::-1]:
                print '%s %s' %(name_list[y][1::], name_list[x][1::])
            if data_list[x][::-1][0:3][::-1] == data_list[y][0:3]:
                print '%s %s' %(name_list[x][1::], name_list[y][1::])

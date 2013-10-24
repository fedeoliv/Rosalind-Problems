# http://rosalind.info/problems/cons/

def read_fasta(collection_dna):
    name, seq = None, []
    
    for line in collection_dna:
        line = line.rstrip()
        
        if line.startswith(">"):
            if name: 
                yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    
    if name: 
        yield (name, ''.join(seq))


list_dna = []

with open('rosalind_cons.txt') as collection_dna:
    for name, sequence in read_fasta(collection_dna):
        list_dna.append(sequence)
length = len(list_dna)

total_seq = len(sequence)

profile_values = [[0 for x in xrange(total_seq)] for y in xrange(4)] 

consensus = ['A','C','G','T']

for x in range(total_seq):
    for y in range(4):
        for z in range(length):
            profile_values[y][x] += list_dna[z][x].count(consensus[y])

cons_string = ""

for x in range(total_seq):
    max_value = 0
    
    for y in range(4):  
        if profile_values[y][x] >= profile_values[max_value][x]:
            max_value = y       
            
    if max_value == 0:
        cons_string += 'A'
    elif max_value == 1:
        cons_string += 'C'
    elif max_value == 2:
        cons_string += 'G'
    elif max_value == 3:
        cons_string += 'T'


print('%s\n%s\n%s\n%s\n%s' % (cons_string, 'A: '+ str(profile_values[0]).strip('[]').replace(',',''),
                              'C: '+str(profile_values[1]).strip('[]').replace(',',''),
                              'G: '+str(profile_values[2]).strip('[]').replace(',',''),
                              'T: '+str(profile_values[3]).strip('[]').replace(',','')))

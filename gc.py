#http://rosalind.info/problems/gc/

dnaFile = open('rosalind_gc.txt', 'r')
dna_fasta = dnaFile.readlines()
dnaFile.close()

gc_content = {}
info_dna = ''

for elements in dna_fasta:
    if elements[0] == '>':
        info_dna = elements[1:].rstrip()
        gc_content[info_dna] = ''
    else:
        gc_content[info_dna] += elements.rstrip()

for id_content, content in gc_content.iteritems():
    gc_content[id_content] = (float(content.count('G') + content.count('C')) / len(content)) * 100

(max_id, max_gc) = max(list(gc_content.iteritems()), key = lambda item:item[1])

print max_id
print("%.6f" % max_gc)

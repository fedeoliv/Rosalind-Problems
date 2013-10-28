# http://rosalind.info/problems/long/

import re

f = open("rosalind_long.txt", "r")
array = f.readlines()

nodes = {}
node_name_token = None

for k in range(len(array)):
    if re.match('>', array[k]):
        node_name_token = array[k].strip('\n >')
        nodes[node_name_token] = ''
    else:
        nodes[node_name_token] += array[k].strip()

chromosome_length = len(nodes[node_name_token])
combination = nodes[node_name_token]
del nodes[node_name_token]

while nodes != {}:
    for node, dna in nodes.items():
        for length in range(chromosome_length, chromosome_length / 2, -1):
            if dna.endswith(combination[:length]):
                combination = dna + combination[length:]
                del nodes[node]
                break
            if combination.endswith(dna[:length]):
                combination += dna[length:]
                del nodes[node]
                break

print combination

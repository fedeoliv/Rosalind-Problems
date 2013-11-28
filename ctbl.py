from StringIO import StringIO
from Bio import Phylo
import networkx

def get_character_table(t):
    chars = dict() 
    char_matrix = []
    
    t = Phylo.read(StringIO(t), 'newick')
    
    for c in list(t.get_terminals()):
        chars[c.name] = []
    
    net = Phylo.to_networkx(t)
    adj_matrix = networkx.adjacency_matrix(net)
    tchars = []
    
    for node in net.nodes(data=True):
        tchars.append(str(node[0]))
        
    for m in range(len(adj_matrix)): 
        if adj_matrix[m,:].sum() == 3:
            for i in range(m):
                if (i != m) and (adj_matrix[i,:].sum() == 3) \
                and (adj_matrix[i,m] == adj_matrix[m,i]) and (adj_matrix[i,m] == 1):
                    adj_matrix[i,m] = 0
                    adj_matrix[m,i] = 0
                    
                    net = networkx.from_numpy_matrix(adj_matrix)
                    test1 = networkx.connected_components(net)
                    
                    for item in test1[0]:
                        try:
                            chars[tchars[int(item)]].append(1)
                        except:
                            continue
                    for item in test1[1]:
                        try:
                            chars[tchars[int(item)]].append(0)
                        except:
                            continue
                            
                    adj_matrix[i,m] = 1
                    adj_matrix[m,i] = 1
    
    for i in xrange(len(chars.items()[0][1])):
        char_matrix.append([])
        for j in xrange(len(chars)):
            char_matrix[i].append(0)
    
    nn = 0
    
    for _, v in sorted(chars.items()) :
        for j in range(len(v)):
            char_matrix[j][nn] = v[j]
        nn += 1
    
    for i in xrange(len(char_matrix)):
        str1 = ""
        
        for j in xrange(len(char_matrix[i])):
            str1 += str(int(char_matrix[i][j]))
        print str1 
        
if __name__ == '__main__':
    get_character_table('(dog,((elephant,mouse),robot),cat);')

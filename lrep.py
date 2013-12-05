# http://rosalind.info/problems/lrep/

# Common Node class, containing the pair and the node name
class Node:
    def __init__(self, lab):
        self.f = self.t = 0
        self.s = set()
        self.lab = lab

    def __repr__(self):
        return '%s(f=%s, t=%s, s=%s)' % tuple(map(str, (self.lab, self.f, self.t, self.s)))

def get_longest_substring(r, l):
    global longest_length, longest_string
    substring = 0
    
    if r.t == len(dna_string):
        return 1
    
    str_collection.append((r.f, r.t))
    
    for son in r.s:
        substring += get_longest_substring(son, l + r.t - r.f)
        
    if substring >= k and l + r.t - r.f > longest_length:
        longest_string = list(str_collection)
        longest_length = l + r.t - r.f
        
    str_collection.pop()
    
    return substring

if __name__ == '__main__':
    sons = set()
    nodes = {}
    longest_length = 0
    longest_string = []
    str_collection = []
    
    with open('rosalind_lrep.txt') as f:
        dna_string = f.readline().strip()
        k = int(f.readline().strip())
        
        for x in map(str.strip, f.readlines()):
            a, b, location, t_length = x.split()
            
            node_a = nodes.setdefault(a, Node(a))
            node_b = nodes.setdefault(b, Node(b))
            node_b.f = int(location) - 1
            node_b.t = int(location) + int(t_length) - 1
            
            node_a.s.add(node_b)
            sons.add(node_b)
            
        root = (set(nodes.values()) - sons).pop()
        
    get_longest_substring(root, 0)
    
    print ''.join(dna_string[i:j] for (i, j) in longest_string)

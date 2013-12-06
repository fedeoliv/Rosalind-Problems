# http://rosalind.info/problems/mend/

class Node:
    def __init__(self, par):
        self.p = par
        self.s = set()
        self.lab = ''
        self.probs = {}
        nodes.append(self)

    def __repr__(self):
        return '%s(s=%s)' % (self.lab or 'Node', self.s)

def get_probabilities(tree):
    class current:
        pos = 0

    dd = {}

    def get_node(par):
        cc = Node(par)
        
        if tree[current.pos] == '(':
            while tree[current.pos] in '(,':
                current.pos += 1
                cc.s.add(get_node(cc))
                
            current.pos += 1
            
        cc.s = tuple(cc.s)
        ff = current.pos
        
        while tree[current.pos] not in '), ;':
            current.pos += 1
            
        nam = tree[ff:current.pos]
        cc.lab = nam
        
        if nam != '':
            dd[nam] = cc
            
        return cc

    return get_node(None), dd

def cnt(cur):
    for son in cur.s:
        cnt(son)
        
    if cur.lab:
        for i in ('AA', 'Aa', 'aa'):
            if i == ''.join(sorted(cur.lab)):
                cur.probs[i] = 1.0
            else:
                cur.probs[i] = 0.0
    else:
        c1 = cur.s[0].probs
        c2 = cur.s[1].probs
        
        # All possible probabilities
        cur.probs['AA'] = c1['AA'] * c2['AA'] + c1['Aa'] * c2['Aa'] / 4 + c1['AA'] * c2['Aa'] / 2 + c1['Aa'] * c2['AA'] / 2
        cur.probs['Aa'] = c1['AA'] * c2['aa'] + c1['aa'] * c2['AA'] + c1['Aa'] * c2['Aa'] / 2 + c1['AA'] * c2['Aa'] / 2 + c1['Aa'] * c2['AA'] / 2 + c1['aa'] * c2['Aa'] / 2 + c1['Aa'] * c2['aa'] / 2
        cur.probs['aa'] = c1['aa'] * c2['aa'] + c1['Aa'] * c2['Aa'] / 4 + c1['aa'] * c2['Aa'] / 2 + c1['Aa'] * c2['aa'] / 2

if __name__ == '__main__':
    nodes = []
    
    with open('rosalind_mend.txt') as f:
        (root, d) = get_probabilities(f.readline().strip())
        cnt(root)
        print root.probs['AA'], root.probs['Aa'], root.probs['aa']

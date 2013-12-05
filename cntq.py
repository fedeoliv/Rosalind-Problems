# http://rosalind.info/problems/cntq/

MODULO = 1000000

class Node:
    idd = 0

    def __init__(self, par):
        self.p = par
        self.s = set()
        self.lab = ''
        self.slcnt = 0
        self.qhere = 0
        Node.idd += 1
        self.idd = Node.idd
        nodes.append(self)

    def __repr__(self):
        return '%s(slcnt=%s, qhere=%s, s=%s)' % (self.lab or 'Node' + str(self.idd), self.slcnt, self.qhere, self.s)

def build_tree(tree):
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

    return (get_node(None), dd)

def counter_ab(cur):
    global blackqsum, resother_ab
    tblack = blackqsum
    cur.slcnt = 0
    for son in cur.s:
        cur.slcnt += counter_ab(son)
    if cur.lab:
        cur.slcnt += 1
    if cur.s:
        cur.qhere = cur.s[0].slcnt * cur.s[1].slcnt + (cur.slcnt - 1) * ((1 if cur.lab else 0))
        if len(cur.s) > 2:
            cur.qhere += (cur.s[1].slcnt + cur.s[0].slcnt) * cur.s[2].slcnt
    resother_ab += tblack * cur.qhere
    blackqsum += cur.qhere
    return cur.slcnt

def counter_cd(cur, a, b):
    global resother_cd
    for i in cur.s:
        counter_cd(i, a + cur.qhere, b + cur.slcnt - i.slcnt)
    resother_cd += (a - b * cur.slcnt) * cur.qhere


if __name__ == '__main__':
    nodes = []
    blackqsum = 0
    resother_ab = 0
    resother_cd = 0
    
    with open('rosalind_cntq.txt') as f:
        n = int(f.readline().strip())
        (root, d) = build_tree(f.readline().strip())

    counter_ab(root)
    counter_cd(root, 0, 0)
    
    print (resother_cd + resother_ab) % MODULO

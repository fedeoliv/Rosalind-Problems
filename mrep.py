# http://rosalind.info/problems/mrep/

class Node:
    def __init__(self):
        self.s = {}

    def __repr__(self):
        return 'Node (d=%s)' % self.s

def ptr(t, l, i):
    for x in t.s:
        stack[i] = x
        ptr(t.s[x], l, i + 1)
        stack[i] = ''
    if i >= 20 and len(t.s) > 1:
        tans.append(''.join(stack))

def ptr2(t, l, i):
    for x in t.s:
        stack2[i] = x
        ptr2(t.s[x], l, i + 1)
        stack2[i] = ''
    if i >= 20 and len(t.s) > 1:
        tans2.append(''.join(stack2))

if __name__ == "__main__":
    with open('rosalind_mrep.txt') as f:
        dna_str = f.readline().strip()
    
    s = dna_str + '$'
    root = Node()
    
    for i in xrange(len(s)):
        cur = root
        for c in s[i:]:
            if not c in cur.s:
                cur.s[c] = Node()
            cur = cur.s[c]
    
    stack = [''] * len(s)
    tans = []
    
    s2 = dna_str[::-1] + '$'
    root2 = Node()
    
    for i in xrange(len(s2)):
        cur = root2
        for c in s2[i:]:
            if not c in cur.s:
                cur.s[c] = Node()
            cur = cur.s[c]
    
    stack2 = [''] * len(s)
    tans2 = []
    
    ptr(root, None, 0)
    ptr2(root2, None, 0)
    stans2 = set(tans2)
    
    for i in tans:
        if i[::-1] in stans2:
            print i

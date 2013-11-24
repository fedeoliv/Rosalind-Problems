from itertools import count

class Trie(object):
    def __init__(self):
        self.counter = count(start = 1)
        self.root = [next(self.counter), {}]

    def insert(self, bp):
        node = self.root
        for ch in bp:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter), {}]
            
            node = node[1][ch]

def format_output(node):
    for ch, node2 in node[1].iteritems():
        print node[0], node2[0], ch
        format_output(node2)
        
def get_adjency_list(bps):
    trie = Trie()
    for bp in bps:
        trie.insert(bp)
    return trie.root

if __name__ == '__main__':
    dataset = open('rosalind_trie.txt').readlines()
    dataset = [l.strip() for l in dataset if l.strip()]
    
    format_output(get_adjency_list(dataset))

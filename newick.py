import string

class Tree:
    def __init__(self,u,vs):
        self.u = u
        self.vs = vs

    def distance(self,w):
        if w == self.u:
            return 0,[w]

        for v in self.vs:
            d,path = v.distance(w)
            if d != -1:
                return d+1,[self.u]+path

        return -1,[]

    def taxa(self):
        ret = set()

        if type(self.u) == type(""):
            ret.add(self.u)

        for v in self.vs:
            ret = ret.union(v.taxa())

        return ret

    def nodes(self):
        ret = set([self])

        for v in self.vs:
            ret = ret.union(v.nodes())

        return ret

    def level_traverse(self,ret=None):
        if ret == None:
            ret = []

        for v in self.vs:
            ret = v.level_traverse(ret)

        ret.append(self.u)

        return ret

    def splits(self):
        if len(self.vs) == 0:
            return []

        taxa = self.taxa()

        ret = []
        for v in self.vs:
            vt = v.taxa()
            delta = taxa.difference(vt)

            r = v.splits() #the split happen in subtrees
            ret += [(L,R.union(delta)) for L,R in r]

            ret.append((vt,delta))

        return ret

    def adj_list(self,father=None,cur=None,children=None):
        if cur == None:
            cur = {}
        if children == None:
            children = {}
        
        cur[self.u] = set()
        children[self.u] = set()
        if father != None:
            cur[self.u].add(father)

        for v in self.vs:
            cur,children = v.adj_list(father=self.u,cur=cur,children=children)
            cur[self.u].add(v.u)
            children[self.u].add(v.u)

        return cur,children

def newick_parse(s):
    def S():
        ret = None

        if s[S.pos] == "(":
            S.pos += 1

            label = S.N
            S.N += 1
            ret = Tree(label,[])

            ret.vs.append(S())
            while s[S.pos] == ",":
                S.pos += 1
                ret.vs.append(S())

            assert s[S.pos] == ")"
            S.pos += 1

            if s[S.pos] in string.ascii_letters or s[S.pos] == "_": # has label
                label = s[S.pos]
                S.pos += 1
                while s[S.pos] in string.ascii_letters or s[S.pos] == "_":
                    label += s[S.pos]
                    S.pos += 1

                ret.u = label

        elif s[S.pos] in string.ascii_letters or s[S.pos] == "_":
            label = s[S.pos]
            S.pos += 1
            while s[S.pos] in string.ascii_letters or s[S.pos] == "_":
                label += s[S.pos]
                S.pos += 1

            ret = Tree(label,[])
        else:
            label = S.N
            S.N += 1
            ret = Tree(label,[])
        
        return ret

    
    S.N = 1
    S.pos = 0
    return S()


def edge_splits(t,taxa):
    splits = t.splits()
    splits = filter(lambda x:len(x[0]) != 1 and len(x[1]) != 1, splits)

    ret = []
    for split in splits:
        s = ""
        for i in range(len(taxa)):
            if taxa[i] in split[0]:
                s += "1"
            else:
                s += "0"

        ret.append(s)

    return ret

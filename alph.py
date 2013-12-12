# http://rosalind.info/problems/alph/
 
# Specific module created separately 
import newick

def distance(s,t):
    ret = 0
 
    for k in range(len(s)):
        if s[k] != t[k]:
            ret += 1

    return ret


def parse_fasta(s):
    s = s.strip()
    lines = s.split()
    dnas = {}
    ckey = ""
    key_seq = []

    for line in lines:
        if line[0] == ">":
            ckey = line[1:]
            key_seq.append(ckey)
            dnas[ckey] = ""
        else:
            dnas[ckey] += line

    return dnas,key_seq

if __name__ == "__main__":
    internal = []
    alphabet = "ATGC-"
    
    with open("rosalind_alph.txt") as f:
        nw = f.readline()
        fst = f.read()
        nw = nw.strip()
    
    tree = newick.newick_parse(nw)
    dnas, key = parse_fasta(fst)
    
    adj_list, children = tree.adj_list()
    ordered = tree.level_traverse()
    
    assert(set(ordered) == set(tree.taxa()))

    for taxon in ordered:
        if tree.u != taxon:
            assert(len(adj_list[taxon]) == len(children[taxon]) + 1)
        else:
            assert(len(adj_list[taxon]) == len(children[taxon]))
    
        if len(adj_list[taxon]) > 1:
            internal.append(taxon)
    
    for taxon in ordered:
        for child in children[taxon]:
            assert(ordered.index(child) < ordered.index(taxon))
            
    dp, pre = {}, {}
    l = len(dnas[key[0]])
    
    for k in range(l):
        dp[k] = {}
        pre[k] = {}
    
        for taxon in internal:
            dp[k][taxon] = {}
            pre[k][taxon] = {}
    
            for a in alphabet:
                dp[k][taxon][a] = 0
                pre[k][taxon][a] = {}
    
                for child in children[taxon]:
                    if len(children[child]) == 0: #leaf node
                        if a != dnas[child][k]:
                            dp[k][taxon][a] += 1
    
                        pre[k][taxon][a][child] = dnas[child][k]
                    else: #another internal node
                        ma = a
                        minc = 0
                        
                        for b in alphabet:
                            if b == a:
                                inc = 0
                            else:
                                inc = 1
    
                            if dp[k][child][ma] + minc > dp[k][child][b] + inc:
                                ma = b
                                minc = inc
    
                        dp[k][taxon][a] += minc + dp[k][child][ma]
                        pre[k][taxon][a][child] = ma
    
    root = tree.u
    ans = 0
    
    for k in range(l):
        ans += min(dp[k][root].values())
    
    print(ans)
        
    result = {}
    
    for k in range(l):
        def reconstruct_dna(node,a):
            result.setdefault(node,"")
            result[node] += a
    
            for child in children[node]:
                reconstruct_dna(child, pre[k][node][a][child])
    
        ra = min(dp[k][root], key = dp[k][root].get)
        reconstruct_dna(root,ra)
    
    for k, v in result.items():
        if k in internal:
            print(">%s" % k)
            print(v)
    
        
    c = 0
    
    for taxon in ordered:
        for child in children[taxon]:
            c += distance(result[taxon],result[child])
    
    assert(c == ans)

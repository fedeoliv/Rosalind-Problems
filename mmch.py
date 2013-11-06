from math import factorial

def get_basepair_edges(rna):
    a, u, g, c = map(rna.count, ["A", "U", "G", "C"])
    
    a = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
    b = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))
    
    return a * b

if __name__ == '__main__':
    print get_basepair_edges("AUGCUUC")

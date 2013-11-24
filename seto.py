def get_sets(n, a, b):
    return [a | b, a & b, a - b, b - a, set(range(1, n + 1)) - a, set(range(1, n + 1)) - b]

def format_output(result):
    b = open('rosalind_seto_out.txt', 'w')
    for r in result:
        print "{" + ', '.join(map(str, r)) + "}"
        b.write("{" + ', '.join(map(str, r)) + "}\n")

def parse(line):
        return [s.strip() for s in line.strip()[1:-1].split(",")]

if __name__ == '__main__':
    n, a, b = open('rosalind_seto.txt').readlines()
    
    n = int(n.strip())
    a = set(map(int, parse(a)))
    b = set(map(int, parse(b)))
    
    format_output(get_sets(n, a, b))

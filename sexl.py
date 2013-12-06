# http://rosalind.info/problems/sexl/

def get_prob_carrier(a):
    b = []
    
    for p in a:
        b.append(2 * (1 - p) * p)
    return ' '.join(['%.3f'% x for x in b])

if __name__ == '__main__':
    dataset = map(float, open('rosalind_sexl.txt').read().strip().split())
    print get_prob_carrier(dataset)

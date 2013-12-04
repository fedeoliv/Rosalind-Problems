# Problem: http://rosalind.info/problems/cunr/
# Unrooted binary trees: http://en.wikipedia.org/wiki/Unrooted_binary_tree

MODULO = 1000000

def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)

if __name__ == '__main__':
    n = int(open('rosalind_cunr.txt').readline())
    
    print double_factorial(2 * n - 5) % MODULO

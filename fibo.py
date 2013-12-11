# http://rosalind.info/problems/fibo/

def get_fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return get_fibonacci(n - 1) + get_fibonacci(n - 2)
    
if __name__ == '__main__':
    n = int(open('rosalind_fibo.txt').read().strip())
    
    print get_fibonacci(n)

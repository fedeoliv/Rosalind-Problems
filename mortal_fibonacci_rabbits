# http://rosalind.info/problems/fibd/

def mortal_fibbonacci(n, l, m=1):
    """
        l = life time of the rabbits
        m = maturity time
    """
    fib_table = []
    
    for i in range(n):
        if i < l:
            if i == 0 or i == 1:
                fib_table.append(1)
            else:
                fib_table.append(fib_table[-1] + fib_table[-2])
        else:
            rabbits = 0
            
            for j in range(i-l, i-m):
                rabbits = rabbits + fib_table[j]
                
            fib_table.append(rabbits)
    return fib_table

with open('rosalind_fibd.txt', 'r') as f:
    n, l = f.readline().split()
    print mortal_fibbonacci(int(n), int(l))[-1]

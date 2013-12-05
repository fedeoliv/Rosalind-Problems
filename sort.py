# http://rosalind.info/problems/sort/

import collections

def get_all_permutations(s):
    for i in xrange(len(s)):
        for j in xrange(i + 2, len(s) + 1):
            yield (s[:i] + s[i:j][::-1] + s[j:], (i + 1, j))

def get_reversal_distance(p1, p2):
    if p1 == p2:
        return 0
    
    target = tuple(p2)
    first = {tuple(p1): 0}
    first_histories = {tuple(p1): ()}
    q = collections.deque((p1, ))
    
    while len(q):
        s = q.popleft()
        c = first[s]
        history = first_histories[s]
        
        for (j, zz) in get_all_permutations(s):
            if j == target:
                return (c + 1, history + (zz, ))
            if not j in first:
                first[j] = c + 1
                first_histories[j] = history + (zz, )
                
                if c != 4:
                    q.append(j)
                    
    second = {tuple(p2): 0}
    second_histories = {tuple(p2): ()}
    target = tuple(p1)
    q = collections.deque((p2, ))
    answer = 100000
    answer_history = ()
    
    while len(q):
        s = q.popleft()
        c = second[s]
        history = second_histories[s]
        
        for (j, zz) in get_all_permutations(s):
            if not j in second:
                second[j] = c + 1
                second_histories[j] = history + (zz, )
                
                if c != 3:
                    q.append(j)
                    
            if j in first:
                if answer > first[j] + second[j]:
                    answer = first[j] + second[j]
                    answer_history = first_histories[j] + second_histories[j][::-1]
                    
    return answer, answer_history

with open('rosalind_sort.txt') as f:
    s = tuple(map(int, f.readline().split()))
    t = tuple(map(int, f.readline().split()))
    
    distance, reversals = get_reversal_distance(s, t)
    
    print distance
    
    for (x, y) in reversals:
        print x, y

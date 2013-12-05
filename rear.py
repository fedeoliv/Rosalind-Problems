# http://rosalind.info/problems/rear/

import collections

def get_all_permutations(s):
    for i in xrange(len(s)):
        for j in xrange(i + 2, len(s) + 1):
            yield s[:i] + s[i:j][::-1] + s[j:]

def get_reversal_distance(p1, p2):
    if p1 == p2:
        return 0
    
    target = tuple(p2)
    fromfirst = {tuple(p1): 0}
    q = collections.deque((p1, ))
    
    while len(q):
        s = q.popleft()
        c = fromfirst[s]
        
        for j in get_all_permutations(s):
            if j == target:
                return c + 1
            
            if not j in fromfirst:
                fromfirst[j] = c + 1
                
                if c != 4:
                    q.append(j)
                    
    fromsecond = {tuple(p2): 0}
    target = tuple(p1)
    q = collections.deque((p2, ))
    answer = 100000
    
    while len(q):
        s = q.popleft()
        c = fromsecond[s]
        
        if c == 4:
            break
        
        for j in get_all_permutations(s):
            if j == target:
                return c + 1
            
            if not j in fromsecond:
                fromsecond[j] = c + 1
                
                if c != 3:
                    q.append(j)
                    
            if j in fromfirst:
                answer = min(answer, fromfirst[j] + fromsecond[j])
    return answer

if __name__ == "__main__":
    distances = []
    
    with open('rosalind_rear.txt') as s:
        dataset = map(str.strip, s.readlines())
    
    for i in xrange(0, len(dataset), 3):
        s = tuple(map(int, dataset[i].split()))
        t = tuple(map(int, dataset[i + 1].split()))
        
        distances.append(get_reversal_distance(t, s))
        
    print ' '.join(map(str, distances))

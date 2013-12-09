# http://rosalind.info/problems/1f/

def compare(pattern,text):
    i,count = 0,0    
    while i < len(pattern):
        if pattern[i] != text[i]:
            count += 1
        i += 1
    return count

def get_positions(pattern,text,d):
    i, result = 0, []
    
    while i < len(text) - len(pattern) + 1:
        if compare(pattern,text[i:i+len(pattern)]) <= d:
            result.append(i)
            
        i += 1
    
    return result

if __name__ == '__main__':
    pattern, text, d = open('rosalind_1f.txt').read().strip().split('\n')
    d = float(d)
    
    result = get_positions(pattern,text,d)
    
    print ' '.join(map(str,result))

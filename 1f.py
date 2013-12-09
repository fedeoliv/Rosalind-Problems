def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    return data
    f.close()

def comparison(pattern,text):
    i,count = 0,0    
    while i < len(pattern):
        if pattern[i] != text[i]:
            count += 1
        i += 1
    return count

def approximate(pattern,text,d):
    i, result = 0, []
    
    while i < len(text)-len(pattern)+1:
        if comparison(pattern,text[i:i+len(pattern)]) <= d:
            result.append(i)
        i += 1
    
    return result

if __name__ == '__main__':
    pattern, text, d = [item.strip() for item in read_file('rosalind_1f.txt')]
    d = float(d)
    result = approximate(pattern,text,d)
    
    print ' '.join(map(str,result))

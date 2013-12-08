# http://rosalind.info/problems/ini/

if __name__ == '__main__':
    s = open('rosalind_ini.txt').readline()
    result = [s.count('A'), s.count('C'), s.count('G'), s.count('T')]
    
    print ' '.join(map(str, result))

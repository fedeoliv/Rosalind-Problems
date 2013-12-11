# http://rosalind.info/problems/meme/

from subprocess import call

# The path can vary in different OS.
# "~/bin/meme.bin" is the path where I installed MEME tools. 
# When we search for protein information, it will be written in "rosalind_meme_output.txt".
# How to install MEME Tools: http://meme.nbcr.net/meme/doc/meme-install.html 
COMMAND = "~/bin/meme.bin rosalind_meme.txt -text -nostatus -protein -minw 20 > rosalind_meme_output.txt"

if __name__ == '__main__':  
    c = call(COMMAND, shell = True)

    with open('rosalind_meme_output.txt') as output:
        while True:
            line = output.readline()
            
            if 'regular expression' in line:
                sep = output.readline()
                reg_expr = output.readline().rstrip()
                break
            
            if not line: break
            
    print (reg_expr)

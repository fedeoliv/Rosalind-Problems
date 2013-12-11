# http://rosalind.info/problems/filt/

# For this problem, you need to install FASTX Toolkit.
# FASTX Download: http://hannonlab.cshl.edu/fastx_toolkit/download.html

from subprocess import call
from Bio import SeqIO

COMMAND = "fastq_quality_filter -Q33 -q {0} -p {1} -i {2} -o rosalind_filt_output.txt"

if __name__ == "__main__":
    with open('rosalind_filt.txt') as dataset:
        q, p = [int(d) for d in dataset.readline().split()]
        
        # We need to write a file similar to the dataset,
        # but without threshold (q) and percentage (p).
        with open('rosalind_filt_input.txt', 'w') as infile:
            for line in dataset.readlines():
                infile.write(line)

    c = call(COMMAND.format(q, p, 'rosalind_filt_input.txt'), shell = True)
    
    with open('rosalind_filt_output.txt') as output:
        seqs = SeqIO.parse(output, 'fastq')
        
        print len(list(seqs))

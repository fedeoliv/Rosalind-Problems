# http://rosalind.info/problems/swat/

from Bio.Emboss.Applications import WaterCommandline
from Bio import ExPASy, SeqIO


if __name__ == "__main__":
    ids = open('rosalind_swat.txt').read().split(' ')

    for i in ids:
        handle = ExPASy.get_sprot_raw(i)
        r = SeqIO.read(handle, "swiss")
        handle.close()
        
        with open(i, 'w') as f:
            SeqIO.write(r, f, 'fasta')

    water_cline = WaterCommandline()
    water_cline.asequence = ids[0]
    water_cline.bsequence = ids[1]
    water_cline.outfile = "rosalind_swat_output.txt"
    water_cline.gapopen = 10
    water_cline.gapextend = 1
    water_cline()

    for line in  open('rosalind_swat_output.txt').readlines():
        if 'Score:' in line:
            print(int(float(line[:-1].split(':')[-1].strip())))

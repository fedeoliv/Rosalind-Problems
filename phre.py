# http://rosalind.info/problems/phre/

from Bio import SeqIO

def get_average(l):
        return sum(l) / float(len(l))

def get_below_threshold(threshold, fastq):
    i = 0
    fastq_collection = SeqIO.parse(fastq, "fastq")        
    
    for record in fastq_collection:
        if get_average(record.letter_annotations["phred_quality"]) < threshold:
            i += 1

    return i

if __name__ == '__main__':
    threshold = int(open('rosalind_phre.txt').readline())
    
    print get_below_threshold(threshold, "rosalind_phre.txt")

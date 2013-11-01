# http://rosalind.info/problems/corr/

import string

substitution = string.maketrans("ACGT", "TGCA")

def hamming_distance(reference, comparison):
    hd = index = 0
    max_index = len(reference)

    while(index < max_index):
        if(index >= len(comparison)):
            return hd
        
        if(reference[index] != comparison[index]):
            hd += 1
            
        index += 1
    return hd

def revert_str(sequence):
    return sequence[::-1].translate(substitution)

if __name__ == "__main__":
    data = []
    repeated = []
    non_repeated = []
    i = 0
    
    data_file = open("rosalind_corr.txt")
    for line in data_file:
        data.append(line.strip())
    data_file.close()

    while i < len(data):
        if data[i] in data[i + 1:] or revert_str(data[i]) in data:
            repeated.append(data[i])
            data = [sequence for sequence in data if sequence != data[i] and
                    sequence != revert_str(data[i])]
        else:
            non_repeated.append(data[i])
            i+= 1
    
    for string in non_repeated:
        broken = False
        
        for candidate in repeated:
            if string == candidate:
                continue
            if hamming_distance(string, candidate) == 1:
                print(string + '->' + candidate)
                broken = True
                break
            if hamming_distance(string, revert_str(candidate)) == 1:
                print(string + '->' + revert_str(candidate))
                broken = True
                break

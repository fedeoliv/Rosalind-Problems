# http://rosalind.info/problems/pdst/

def get_matrix(sequence_list):
    return_matrix = []
    for seq in sequence_list:
        line = []
        for other_seq in sequence_list:
            line.append(float(hamm(seq, other_seq))
                        / min([len(seq), len(other_seq)]))
        return_matrix.append(line)
    for thing in return_matrix:
        for other_thing in  thing:
            print("%1.5f" % other_thing),
        print

def hamm(reference, comparison):
    hamming_distance = abs(len(reference) - len(comparison))
    index = 0
    max_index = min([len(reference), len(comparison)])

    while(index < max_index):
        if(reference[index] != comparison[index]):
            hamming_distance += 1
        index += 1
        
    return hamming_distance

if __name__ == "__main__":
    sequences = []
    labels = []
    lengths = []
    
    data_file = open("rosalind_pdst.txt")
    sequence_counter = -1
    
    for line in data_file:
        if(line[-1] == '\n'):
            line = line[:-1]
        if(line[0].startswith(">")):
            sequence_counter += 1
            labels.append(line[1:])
            sequences.append("")
            lengths.append(0)
        else:
            sequences[sequence_counter] = ''.join([sequences[sequence_counter], line])
            lengths[sequence_counter] += len(line)
            
    data_file.close()

    get_matrix(sequences)

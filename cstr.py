# http://rosalind.info/problems/cstr/

def get_character_table(dna_strings):
    str_collection = []
    # filter: return those items of sequence for which function(item) is true.  
    # If function is None, return the items that are true.
    # True = 1 and False = 0.
    positions = [''.join(map(str, map(int, map(s[0].__eq__, s))))
                   for s in map(''.join, zip(*filter(None, dna_strings)))]
    
    for k in set(positions):
        if sum(map(int, k)) not in (0, 1, len(k), len(k) - 1):
            str_collection.append(k)
    
    return str_collection 
                 
if __name__ == '__main__':
    with open('rosalind_cstr.txt') as f:
        # Splitting the dna strings
        dna_strings = map(str.strip, f.readlines())
        
        print "\n".join(str(x) for x in get_character_table(dna_strings))

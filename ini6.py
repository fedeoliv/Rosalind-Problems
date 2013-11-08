# http://rosalind.info/problems/ini6/

from collections import Counter

def count_words(str_input):
    list_str = []
    
    for word in str_input.split(' '):
        list_str.append(word)
    
    dictionary = Counter(list_str)
    
    for str_value, quantity in dictionary.items():
        print str_value, quantity
    
if __name__ == "__main__":
    count_words("We tried list and we tried dicts also we tried Zen")

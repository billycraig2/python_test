from functools import reduce

def longest_word(message):
    # joins letters that are spaces or alphabet to a string and then splits by spaces
    words = ''.join(filter(lambda c : c.isspace() or c.isalpha(), message)).split()
    # loops through words and compares lengths
    longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
    return longest_word
        
    
message = input('Input: ')
print(longest_word(message))

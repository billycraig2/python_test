def find_longest_word(message):
    longest_word = ''
    current_word = ''

    # loop through each letter of the input message
    for letter in message+' ':
    # condition to check if alphabet letter
        if letter.isalpha():
            current_word = current_word + letter
        else:
            # condition to check if the current word is longer than longest word
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ''

    print (longest_word)
        
    
message = input('Input: ')
find_longest_word(message)

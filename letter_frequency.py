message = input("Input: ").lower
message_dict = {}

# looping through each letter of the input 
for letter in message:
    # condition to check if the letter already exists in dict
    if letter in message_dict.keys():
        message_dict[letter] = message_dict[letter] + 1
    else:
        message_dict[letter] = 1

# printing the frequency of each letter in the message
for key in message_dict:
    print("Frequency of " + key + " is " + str(message_dict[key]))
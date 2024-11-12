input = [1, 2, 3, 4, 5, 6, 7]

# go through each element and swap to position
for i in range(len(input)//2):
    j = len(input) - 1 - i
    input[i], input[j] = input[j], input[i]

print(input)
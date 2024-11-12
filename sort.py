input = [1,2,3,2,2,2,3,1,1]

# go through each element if the element to the right is bigger it swaps them
for i in input:
    for j in input:
        if input[i] < input[j]:
            input[j], input[i] = input[i], input[j]
        else:
            continue

print(input)
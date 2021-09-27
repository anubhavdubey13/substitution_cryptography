# Storing alphabets in a list
list_of_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print(list_of_alphabet['a'])

# Taking input from user
# Text
original_text = input('Enter the text:').lower()
#print(original_text)

# To shift by
push_by = int(input('Number of spaces to be shifted'))

# Initializing an empty list to store the results from iteration
output = []

# What is left: 1. how to shift using push_by to create the encrypted code
for o in original_text:
    if o in list_of_alphabet:
        o = list_of_alphabet[list_of_alphabet.index(o)]
        output.append(o)

print(''.join(output))


if 'o' in list_of_alphabet:
    print(list_of_alphabet[list_of_alphabet.index('o')])
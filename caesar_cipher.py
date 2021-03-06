# Function for Encryption using Caesar Cipher

def caesar_cipher_encrypt(text, key):
    '''text: str, key: int'''
    # reference list
    list_of_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # transforming inputs
    original_text = text.lower()
    push_by = key % 26
    # initializing storage list
    output = []
    # Encryption
    for o in original_text:
        if o in list_of_alphabet:
            if list_of_alphabet.index(o) + push_by < 26:
                o = list_of_alphabet[list_of_alphabet.index(o) + push_by]
            else:
                o = list_of_alphabet[list_of_alphabet.index(o) + push_by - 26]
                #print(o)
            output.append(o)
        else:
            output.append(o)

    return ''.join(output)
    
caesar_cipher_encrypt('Love you zindagi!', 13)

# Next Step: Decryption
def caesar_cipher_decrypt(text, key):
    '''text: str, key: int'''
    # reference list
    list_of_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # transforming inputs
    original_text = text.lower()
    push_by = -(key % 26)
    # initializing storage list
    output = []
    # Encryption
    for o in original_text:
        if o in list_of_alphabet:
            if list_of_alphabet.index(o) + push_by < 26:
                o = list_of_alphabet[list_of_alphabet.index(o) + push_by]
            else:
                o = list_of_alphabet[list_of_alphabet.index(o) + push_by - 26]
                #print(o)
            output.append(o)
        else:
            output.append(o)

    return ''.join(output)

caesar_cipher_decrypt('ybir lbh mvaqntv!', 13)

# Next Step: Decryption without key


#================= PRE-FUNCTION CODE ================================================
    
# Storing alphabets in a list
list_of_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print(list_of_alphabet['a'])

# Taking input from user
# Text
original_text = input('Enter the text: ').lower()
#print(original_text)

# To shift by
spaces = int(input('Number of spaces to be shifted: '))

# Not needed 
#if spaces < 0:
 #   push_by = 26 + spaces
#else:
 #   push_by = spaces

push_by = spaces%26

# Initializing an empty list to store the results from iteration
output = []

# I think division is a much better approach. Need to figure out dealing with reminders
# Encryption
for o in original_text:
    if o in list_of_alphabet:
        if list_of_alphabet.index(o) + push_by < 26:
            o = list_of_alphabet[list_of_alphabet.index(o) + push_by]
            #print(o)
        else:
            o = list_of_alphabet[list_of_alphabet.index(o) + push_by - 26]
            #print(o)
        output.append(o)
    else:
        output.append(o)

print(''.join(output))


#========= Rough Work ===============
if 'o' in list_of_alphabet:
    print(list_of_alphabet[list_of_alphabet.index('o') + 12 - 26])
    
    

push = -3
push_you = 26 + push
print(list_of_alphabet[list_of_alphabet.index('a') + push_you])
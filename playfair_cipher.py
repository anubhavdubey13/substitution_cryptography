# Playfair cipher
# https://www.geeksforgeeks.org/playfair-cipher-with-examples/

# Missing stuff:
    # 1. Dealing with j
    # 2. Works only for single words. Altering it for spaces, punctuation etc.

def playfair_encrypt(plain_text):
    
    # importing libraries
    import numpy as np
    import random
    
    # list of alphabets excluding j
    list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Create key if user doesn't pass it
    l = []
    random.shuffle(list_letters)
    for i in range(0,5,1):
        l.append(list_letters[i*5:(i+1)*5])
    key = np.array(l)
    
    # Printing it for reference
    print('Store the key for decryption:', '\n', key)
    
    # Inserting 'x'/'z' between consecutive letters
    i = 0
    while i < len(plain_text) - 1:
        if plain_text[i] == plain_text[i+1]:
            if plain_text[i] != 'x':
                plain_text = plain_text[:i+1] + 'x' + plain_text[i+1:]
            else:
                plain_text = plain_text[:i+1] + 'z' + plain_text[i+1:]
        i += 1
    
    # Adding 'z' for odd length
    if len(plain_text)%2 == 0:
        plain_text = plain_text
    else:
        plain_text += 'z'
    
    # Splitting in pairs
    i=0
    pieces = []
    while i < len(plain_text)/2:
        pieces.append(plain_text[2*i:2*i+2])
        i += 1
    
    # Playfair Algorithm
    encrypted = []
    for p in pieces:
        lr = []
        lc = []
        for q in p:
            r, c = np.where(key==q)
            r = int(r)
            #print(r)
            c = int(c)
            #print(c)
            lr.append(r)
            lc.append(c)
        if lc[0] == lc[1]:
            cipher = key[(lr[0]+1) % 5][lc[0]] + key[(lr[1]+1) % 5][lc[1]]
        elif lr[0] == lr[1]:
            cipher = key[lr[0]][(lc[0]+1) % 5] + key[lr[1]][(lc[1]+1) % 5]           
        else:
            cipher = key[lr[0]][lc[1]] + key[lr[1]][lc[0]]
        encrypted.append(cipher)
    return print(''.join(encrypted))

playfair_encrypt('jacuzi')

#=============================ROUGH WORK ==============================
# exclude j straightaway
list_of_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Step 1: Trying to create the 5X5 matrix key
import numpy as np

# Chanced upon shuffle function in random library.
import random

# random.shuffle(list_of_alphabets)

# x=np.array([[0,1,2],[4,8,5]])
# x[1][2]
# y = [[0,1,2],[4,8,5]]

# l1 = []
# l2 = []
# random.shuffle(list_of_alphabets)
# for l in list_of_alphabets:  
#     for i in range(0,5,1):
#         for j in range(0,5,1):
#             l1.append(l)
#         #l2.append(l1)
# print(l2)

# Simple does it. Mostly.
l1 = []
l2 = []
random.shuffle(list_of_alphabets)
for i in range(0,5,1):
    l1.append(list_of_alphabets[i*5:(i+1)*5])
key = np.array(l1)
print(key)


# Convert this to take input
plain_text = 'hexxo'

# Adding 'z' for odd length
if len(plain_text)%2 == 0:
    plain_text = plain_text
else:
    plain_text += 'z'
print(plain_text)

# # Split and add 'x' in case of consecutive elements
i = 0
while i < len(plain_text) - 1:
    if plain_text[i] == plain_text[i+1]:
        if plain_text[i] != 'x':
            plain_text = plain_text[:i+1] + 'x' + plain_text[i+1:]
        else:
            plain_text = plain_text[:i+1] + 'z' + plain_text[i+1:]
    i += 1
print(plain_text)

# Splitting in pairs
i=0
pieces = []
while i < len(plain_text)/2:
    pieces.append(plain_text[2*i:2*i+2])
    i += 1
print(pieces)

# Encryption
# Rules
# 1. If both the letters are in the same column: Take the letter below each one
encrypted = []
for p in pieces:
    lr = []
    lc = []
    for q in p:
        r, c = np.where(key==q)
        r = int(r)
        #print(r)
        c = int(c)
        #print(c)
        lr.append(r)
        lc.append(c)
    if lc[0] == lc[1]:
        cipher = key[(lr[0]+1) % 5][lc[0]] + key[(lr[1]+1) % 5][lc[1]]
    else:
        cipher = p
    encrypted.append(cipher)
pieces_1 = encrypted  
print(''.join(encrypted))
        
# 2. If both the letters are in the same row: Take the letter to the right of each one
encrypted = []
for p in pieces_1:
    lr = []
    lc = []
    for q in p:
        r, c = np.where(key==q)
        r = int(r)
        #print(r)
        c = int(c)
        #print(c)
        lr.append(r)
        lc.append(c)
    if lr[0] == lr[1]:
        cipher = key[lr[0]][(lc[0]+1) % 5] + key[lr[1]][(lc[1]+1) % 5]
    else:
        cipher = p
    encrypted.append(cipher)
pieces_2 = encrypted   
print(''.join(encrypted))

# 3. If neither of the above rules is true: Form a rectangle with the two letters and 
# take the letters on the horizontal opposite corner of the rectangle.        

# Will need to combine all these into a single step because we gotta use if-else
# which reminds me that Python 4 is out and they have a switch statement 
# probably like JS. Which I studied in 1 week 15 months ago. Just bragging

#cipher = key[lr[0]][lc[1]] + key[lr[1]][lc[0]]

        
        
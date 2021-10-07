# Playfair cipher
# https://www.geeksforgeeks.org/playfair-cipher-with-examples/

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
# i = 0
# while i < len(plain_text) - 1:
#     if plain_text[i] == plain_text[i+1]:
#         if plain_text[i] != 'x':
#             plain_text = plain_text[:i+1] + 'x' + plain_text[i+1:]
#         else:
#             plain_text = plain_text[:i+1] + 'z' + plain_text[i+1:]
#     i += 1
# print(plain_text)

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
    if lc[0] == lc[1]:
        cipher = key[lr[0]][(lc[0]+1) % 5] + key[lr[1]][(lc[1]+1) % 5]
    else:
        cipher = p
    encrypted.append(cipher)
pieces_2 = encrypted   
print(''.join(encrypted))

# 3. If neither of the above rules is true: Form a rectangle with the two letters and 
# take the letters on the horizontal opposite corner of the rectangle.        


        
        
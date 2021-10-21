# Hill Cipher
# Some Algebra coming

import numpy as np

def hill_encrypt():
    
    pass

# Step 1: Generate a Random Key
ORDER = 3

def random_key():
    
    import random
    
    key = np.array([[random.randint(0,26) for i in range(ORDER)] for j in range(ORDER)])
    # probably my first time using list comprehension
    
    return key

# Didn't work. Had to make some changes
# # Step 2: Divide Input text into arrays of size Order*1
# def input_format(plain_text):
#     # Removing spaces between words. Would come back during decryption as this might causes issues
#     pt = ''.join(str.split(plain_text.lower()))
    
#     # If the input isn't compatible for a 3*n matrix then add x's at the end
#     if len(pt) % 3 != 0:
#         pt = pt + 'x'*(len(pt)%3)
        
#     # Dividing input across 3*n matrix where n = len(pt)%3
#     master = np.array([[] for i in range(ORDER)]) # Empty list of order n*ORDER
#     indices = np.array([[] for i in range(ORDER)]) # Same as above but end goal to get indices
    
#     # List of alphabets (for indices)
#     list_of_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
#                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#     # for j in range(len(pt)):
#     #     for i in range(ORDER):
#     #         master[i].append(pt[j])
        
#     for i in range(ORDER):
#         j = i
#         while j < len(pt):
#             master[i][j] = pt[j]
#             j += 3
    
#     for i in range(ORDER):
#         j = i
#         while j < len(pt):
#             indices[i][j] = list_of_alphabets.index(pt[j])
#             j += 3
    
#     # final_text = np.array(master, dtype = object)
#     # final_matrix = np.array(indices, dtype = float)
    
#     final_text = master
#     final_matrix = indices    
    
#     return final_text, final_matrix


# Step 2: Divide Input text into arrays of size Order*1
def input_format(plain_text):
    # Removing spaces between words. Would come back during decryption as this might causes issues
    pt = ''.join(str.split(plain_text.lower()))
    
    # If the input isn't compatible for a 3*n matrix then add x's at the end
    if len(pt) % 3 != 0:
        pt = pt + 'x'*(len(pt)%3)
        
    # Dividing input across 3*n matrix where n = len(pt)%3
    master = [[] for i in range(ORDER)] # Empty list of order n*ORDER
    indices = np.array([np.zeros(int(len(pt)/3)) for i in range(ORDER)]) # Same as above but end goal to get indices
    
    # List of alphabets (for indices)
    list_of_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # for j in range(len(pt)):
    #     for i in range(ORDER):
    #         master[i].append(pt[j])
        
    for i in range(ORDER):
        j = i
        while j < len(pt):
            master[i].append(pt[j])
            j += 3
    
    for i in range(ORDER):
       # j = i
        for j in range(int(len(pt)/3)):
            indices[i][j] = list_of_alphabets.index(master[i][j])
            #j += 3
    
    # final_text = np.array(master, dtype = object)
    # final_matrix = np.array(indices, dtype = float)
    
    final_text = master
    final_matrix = indices    
    
    return final_text, final_matrix

# Next steps: multiplying key and final_matrix
# Converting resultant matrix back to letters
# Figure out a way to take care of spaces in text

# Step 3: cipher
def create_cipher(key, final_matrix):
    
    code_indices = np.dot(key, final_matrix)%26
    print(code_indices)
    r, c = code_indices.shape
    
    # List of alphabets (for letters from indices)
    list_of_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    the_secret = [[] for i in range(ORDER)]
    
    for i in range(r):
        print(i)
        for j in range(c):
            print(j) # DEBUG THIS: BASICALLY USE APPEND BECAUSE OTHER MEANS ARE INEFFECTIVE
            the_secret[i][j] = list_of_alphabets[int(code_indices[i][j])]
            print(the_secret)
            
    return the_secret
    

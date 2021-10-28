# Hill Cipher
# Some Algebra coming

import numpy as np

def hill_encrypt(plain_text, key = None, ORDER = 3):
    
    # key
    if key == None:
        key = random_key()
    #print(key)
    # format input
    final_text, final_matrix = input_format(plain_text)
    #print(final_text, final_matrix)
    # cipher
    the_secret, code_init = create_cipher(key, final_matrix)
    #print(the_secret, code_init)
    # join the secret
    y = join_the_secret(the_secret)
    #print(y)
    # sanity check
    #invert_to_check(key, code_init, final_matrix) # something wrong here. Some other day
    final = spaces(plain_text, y)
    return final, key, code_init

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
        pt = pt + 'x'*(3-len(pt)%3)
        
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

# Next steps: multiplying key and final_matrix - done
# Converting resultant matrix back to letters - done
# Recombining the msg - done
# Figure out a way to take care of spaces in text 
# Next step: find inverse to check if answer correct -  done

# Step 3: cipher
def create_cipher(key, final_matrix):
    
    code_init = np.round(np.dot(key, final_matrix)) 
    code_indices = np.round(np.dot(key, final_matrix))%26
    #print(code_indices)
    r, c = code_indices.shape
    
    # List of alphabets (for letters from indices)
    list_of_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    the_secret = [[] for i in range(ORDER)]
    
    for i in range(r):
        #print(i)
        for j in range(c):
           # print(j)
            the_secret[i].append(list_of_alphabets[int(code_indices[i][j])])
            #print(the_secret)
            
    return the_secret, code_init

# Step 4: Combo
def join_the_secret(the_secret):
    x = []
    for i in range(len(the_secret)):
        x.append(''.join(the_secret[i]))    
        
    y = ''
    for i in range(int(len(''.join(x))/3)):
        for j in range(len(x)):
            y += x[j][i]
            
    return y

# Step 5: Inverse to check: There is some issue here. Commenting it out from the main func
def invert_to_check(key, code_init, final_matrix):
    
    inverted_key = np.linalg.inv(key)
    
    check = np.dot(inverted_key, code_init)
    
    check[check <= 0] = 0
    
    # if np.array_equal(final_matrix, check):
    #     return check, True
    # else:
    #     print('Something went wrong during inverse check')
    #     return check
    return check
    
# seems good to go except the space part that would be handy in decrpytion
# Step 6: Identifying spaces and inserting them in code
def spaces(plain_text, y):
    
    indices = []
    
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            indices.append(i)
            
    for i in indices:
        y = y[:i] + ' ' + y[i:]

    return y

#==================================== Decryption with Key =============================
# Steps:
    # 1. convert ciphertext to matrix
    # 2. Matrix to matrix of indices
    # 3. Invert key then multiply with matrix of indices (invert_to_check algo used)
    # 4. Resultant matrix to matrix of elements
    # 5. Check for x towards the end
    # 6. use spaces to insert proper spaces


# i wrote the function but woh udd gya :(
# will redo tom

# A very bad solution is needing code_init
# I take modulo and doing reverse w/o any idea about code_init gonna be difficult

# Rudimentary solution
def hill_decrypt(cipher_text, key, code_init):
    # basically no need for cipher_text
    s, ci = create_cipher(np.linalg.inv(key), code_init)
    y = join_the_secret(s)
    plain = spaces(cipher_text, y)
    return plain

# I am currently laughing at this solution.
# Need to figure out a way to break this code

# There is something called as inverse modulo. Seems that needs to be used.

# So euclidea method to solve equation

def mod_26(a):
    if a == 1:
        print('does not work for a = 1')
    else:

        b = 26
        while a !=0:
            print(a,b)
            c = b%a
            b = a
            a = c
            print(c)

    return None

def mod_rem(a, b = 26):
    l = []
    m = []
    while a != 0:
        l.append(b)
        c = b%a
        d = b//a
        b = a
        a = c
        m.append(d)
    return l, m

# I really wish to look up the code online but will try to figure out myself
l, m = mod_rem(17)
if l[-2] - (l[-2]//l[-1])*l[-1] == 1:
    


#==============ROUGH OUTPUT==========================
# mod_rem(17, 29)
# Out[40]: [29, 17, 12, 5, 2]

# 12%26
# Out[41]: 12

# 12%29
# Out[42]: 12

# -12%29
# Out[43]: 17

# -3%26
# Out[44]: 23

# 5 - 2*2
# Out[45]: 1

# 5 - 2*(12-2*5)
# Out[46]: 1

# (17-12) - 2*(12-2*5)
# Out[47]: 1

# (17-(29-17)) - 2*((29-17)-2*(17-12))
# Out[48]: 1

# (17-(29-17)) - 2*((29-17)-2*(17-(29-17)))
# Out[49]: 1

# (2*17-29) - 2*((29-17)-2*(2*17-29))
# Out[50]: 1

# (2*17-29)
#  - 2*((29-17)-4*17-2*29+2*17)
#   File "C:\Users\admin\AppData\Local\Temp/ipykernel_13092/3648945413.py", line 2
#     - 2*((29-17)-4*17-2*29+2*17)
#     ^
# IndentationError: unexpected indent


# (2*17-29) - 2*((29-17)-4*17-2*29+2*17)
# Out[52]: 165

# (2*17-29) - 2*((29-17)-4*17-2*29)
# Out[53]: 233

# (2*17-29) - 2*((29-17)-2*(2*17-29))
# Out[54]: 1

# (2*17-29) - 2*((29-17)-4*17+2*29)
# Out[55]: 1

# (2*17-29) - 2*(-5*17+3*29)
# Out[56]: 1

# (2*17-29) + 10*17-6*29
# Out[57]: 1

# 12*17-7*29
# Out[58]: 1
            
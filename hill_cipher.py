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

# Step 2: Divide Input text into arrays of size Order*1
def input_format(plain_text):
    # Removing spaces between words. Would come back during decryption as this might causes issues
    pt = ''.join(str.split(plain_text))
    
    # If the input isn't compatible for a 3*n matrix then add x's at the end
    if len(pt) % 3 != 0:
        pt = pt + 'x'*(len(pt)%3)
        
    # Dividing input across 3*n matrix where n = len(pt)%3
    master = [[] for i in range(ORDER)] # Empty list of order n*ORDER
    
    # for j in range(len(pt)):
    #     for i in range(ORDER):
    #         master[i].append(pt[j])
        
    for i in range(ORDER):
        j = i
        while j < len(pt):
            master[i].append(pt[j])
            j += 3
    
    final_text = np.array(master)
    return final_text
    

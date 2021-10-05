# Playfair cipher
# https://www.geeksforgeeks.org/playfair-cipher-with-examples/

list_of_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Step 1: Trying to create the 5X5 matrix key
import numpy as np

# Chanced upon shuffle function in random library.
import random
random.shuffle(list_of_alphabets)

x=np.array([[0,1,2],[4,8,5]])
x[1][2]
y = [[0,1,2],[4,8,5]]



l1 = []
l2 = []
random.shuffle(list_of_alphabets)
for l in list_of_alphabets:  
    for i in range(0,5,1):
        for j in range(0,5,1):
            l1.append(l)
        #l2.append(l1)
print(l2)

# Simple does it. Mostly.
l1 = []
l2 = []
random.shuffle(list_of_alphabets)
for i in range(0,5,1):
    l1.append(list_of_alphabets[i*5:(i+1)*5])
    #l2.append(l1)
print(np.array(l1))
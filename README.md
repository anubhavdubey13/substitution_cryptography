# substitution_cryptography
Trying various substitution cryptography techniques here.

According to Wikipedia:
In cryptography, a substitution cipher is a method of encrypting in which units of plaintext are replaced with the ciphertext, in a defined manner, with the help of a key; the "units" may be single letters, pairs of letters, triplets of letters, mixtures of the above, and so forth.

Starting with the simplest of them all: 
1. Caesar Cipher: The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet.)(https://en.wikipedia.org/wiki/Caesar_cipher)
2. Playfair Cipher: Uses a 5 by 5 table containing a key word or phrase. Memorization of the keyword and 4 simple rules was required to create the 5 by 5 table and use the cipher.(https://en.wikipedia.org/wiki/Playfair_cipher)
3. Hill Cipher: Each letter is represented by a number modulo 26. To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26. To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption. (https://en.wikipedia.org/wiki/Hill_cipher)

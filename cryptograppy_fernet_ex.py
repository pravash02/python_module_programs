'''
Cryptography is the practice of securing useful information while
transmitting from one computer to another or storing data on a computer.
Cryptography deals with the encryption of plaintext into ciphertext and
decryption of ciphertext into plaintext.

'''

from cryptography.fernet import Fernet

# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
'''
This method generates a new fernet key. 
The key must be kept safe as it is the most important component 
to decrypt the ciphertext.
'''
f = Fernet(key)
print(f)

# the plaintext is converted to ciphertext
'''
"Fernet token” which is basically the ciphertext. 
The encrypted token also contains the current timestamp 
when it was generated in plaintext. 
The encrypt method throws an exception if the data is not in bytes.
'''
token = f.encrypt(b"welcome to geeksforgeeks")

# display the ciphertext
print(token)

# decrypting the ciphertext
d = f.decrypt(token)
print(d)

# display the plaintext and the decode() method
# converts it from byte to string
print(d.decode())

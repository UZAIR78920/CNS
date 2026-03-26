# pip install pycryptodomex
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
# Key must be exactly 8 bytes for DES
key = b'ABCDEFGH'
# Create DES object in ECB mode
des = DES.new(key, DES.MODE_ECB)
# Input message
plaintext = input("Enter Plain Text: ")
# Encryption
ciphertext = des.encrypt(pad(plaintext.encode(), 8))
print("Encrypted Text:", ciphertext)
# Decryption
decrypted_text = unpad(des.decrypt(ciphertext), 8)
print("Decrypted Text:", decrypted_text.decode())

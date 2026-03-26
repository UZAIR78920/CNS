def encrypt(text,shift):
    result=""
    for ch in text:
        if ch ==" ":
            result+=" "
        elif ch.isupper():
            result+=chr((ord(ch) +shift - 65) % 26 + 65)
        elif ch.islower():
            result+=chr((ord(ch) +shift - 97) % 26 + 97)
        else:
            result+=ch
    return result
def decrypt(text,shift):
    result=""
    for ch in text:
        if ch ==" ":
            result+=" "
        elif ch.isupper():
            result+=chr((ord(ch) -shift - 65) % 26 + 65)
        elif ch.islower():
            result+=chr((ord(ch) -shift - 97) % 26 + 97)
        else:
            result+=ch
    return result
# Main Program
plaintext=input("Enter Plain Text: ")
shift=int(input("Entershift Value: "))
ciphertext=encrypt(plaintext,shift)
print("Encrypted Text:", ciphertext)
decryptedtext=decrypt(ciphertext,shift)
print("Decrypted Text:", decryptedtext)

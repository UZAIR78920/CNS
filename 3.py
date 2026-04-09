import math
# Function to check coprime
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None
# Step 1: Input two prime numbers
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
# Step 2: Compute n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)
# Step 3: Choose public key e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1
# Step 4: Compute private key d
d = mod_inverse(e, phi)
# Display keys
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
# Step 5: Input message
message = int(input("Enter message (numeric value): "))
# Encryption
ciphertext = pow(message, e, n)
print("Encrypted Message:", ciphertext)
# Decryption
decrypted_message = pow(ciphertext, d, n)
print("Decrypted Message:", decrypted_message)

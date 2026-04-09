p=int(input("Enter a prime number (p): "))
g=int(input("Enter a primite root of p (g): "))
a=int(input("Enter private key of User A: "))
b=int(input("Enter private key of User B: "))
A=pow(g,a,p)
B=pow(g,b,p)
print("public key of user A:",A)
print("public key of user B:",B)
key_A=pow(B,a,p)
Key_B=pow(A,b,p)
print(key_A)
print(Key_B)

# Enter a prime number (p): 11
# Enter a primite root of p (g): 2
# Enter private key of User A: 8
# Enter private key of User B: 4
# public key of user A: 3
# public key of user B: 5
# 4
# 4

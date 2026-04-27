p = 23   # prime number
g = 5    # generator

a = int(input("Enter private key of User1: "))
b = int(input("Enter private key of User2: "))

# Public values
A = pow(g, a, p)
B = pow(g, b, p)

# Secret keys
k1 = pow(B, a, p)
k2 = pow(A, b, p)

print("Public key of User1:", A)
print("Public key of User2:", B)

print("Secret key for User1:", k1)
print("Secret key for User2:", k2)
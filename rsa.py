p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
phi = (p-1) * (q-1)

e = int(input("Enter e: "))

# find d
d = 0
for i in range(1, phi):
    if (i * e) % phi == 1:
        d = i
        break

msg = int(input("Enter message (number): "))

# Encryption
c = (msg ** e) % n

# Decryption
m = (c ** d) % n

print("Public Key (e,n):", (e, n))
print("Private Key (d,n):", (d, n))
print("Encrypted:", c)
print("Decrypted:", m)
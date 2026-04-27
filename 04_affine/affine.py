text = input("Enter text: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))
choice = int(input("1 Encrypt 2 Decrypt: "))

ainv = -1
for i in range(26):
    if (a * i) % 26 == 1:
        ainv = i

result = ""

for ch in text:
    if ch.isalpha():
        x = ord(ch) - 65

        if choice == 1:
            y = (a * x + b) % 26
        else:
            y = (ainv * (x - b)) % 26

        result += chr(y + 65)
    else:
        result += ch

print(result)
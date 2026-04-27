text = input("Enter text: ").upper()
key = int(input("Enter key: "))
choice = int(input("1 Encrypt 2 Decrypt: "))

inv = -1
for i in range(26):
    if (key * i) % 26 == 1:
        inv = i

result = ""

for ch in text:
    if ch.isalpha():
        x = ord(ch) - 65
        if choice == 1:
            y = (x * key) % 26
        else:
            y = (x * inv) % 26
        result += chr(y + 65)
    else:
        result += ch

print(result)
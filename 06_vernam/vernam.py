text = input("Enter text: ").upper()
key = input("Enter key same length: ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))

result = ""

for i in range(len(text)):
    a = ord(text[i]) - 65
    b = ord(key[i]) - 65

    if choice == 1:
        c = (a + b) % 26
    else:
        c = (a - b) % 26

    result += chr(c + 65)

print(result)
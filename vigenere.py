text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))

result = ""
j = 0

for ch in text:
    if ch.isalpha():
        a = ord(ch) - 65
        b = ord(key[j % len(key)]) - 65

        if choice == 1:
            c = (a + b) % 26
        else:
            c = (a - b) % 26

        result += chr(c + 65)
        j += 1
    else:
        result += ch

print(result)
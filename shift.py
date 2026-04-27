text = input("Enter text: ").upper()
key = int(input("Enter key: "))
choice = int(input("1 Encrypt 2 Decrypt: "))

result = ""

for ch in text:
    if ch.isalpha():
        if choice == 1:
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        else:
            result += chr((ord(ch) - 65 - key) % 26 + 65)
    else:
        result += ch

print(result)
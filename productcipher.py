choice = input("Enter E for Encryption or D for Decryption: ").upper()

text = input("Enter text: ").upper()

shift = 3

if choice == 'E':
    
    sub = ""
    for ch in text:
        if ch.isalpha():
            sub += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            sub += ch

    
    cipher = sub[::-1]

    print("After Substitution:", sub)
    print("Cipher Text:", cipher)

elif choice == 'D':
    
    rev = text[::-1]

    
    plain = ""
    for ch in rev:
        if ch.isalpha():
            plain += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            plain += ch

    print("After Reverse:", rev)
    print("Decrypted Text:", plain)

else:
    print("Invalid choice")
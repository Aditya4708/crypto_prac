key = [[3,3],[2,5]]
inv = [[15,17],[20,9]]

text = input("Enter text (even letters): ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))

use = key
if choice == 2:
    use = inv

result = ""

for i in range(0, len(text), 2):
    a = ord(text[i]) - 65
    b = ord(text[i+1]) - 65

    x = (use[0][0]*a + use[0][1]*b) % 26
    y = (use[1][0]*a + use[1][1]*b) % 26

    result += chr(x + 65)
    result += chr(y + 65)

print(result)
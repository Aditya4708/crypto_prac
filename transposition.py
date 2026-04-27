text = input("Enter text: ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))

if choice == 1:
    even = ""
    odd = ""

    for i in range(len(text)):
        if (i + 1) % 2 == 0:
            even += text[i]
        else:
            odd += text[i]

    print(even + odd)

else:
    n = len(text)
    e = n // 2
    o = n - e

    even = text[:e]
    odd = text[e:]

    res = ""
    x = y = 0

    for i in range(n):
        if (i + 1) % 2 == 0:
            res += even[x]
            x += 1
        else:
            res += odd[y]
            y += 1

    print(res)
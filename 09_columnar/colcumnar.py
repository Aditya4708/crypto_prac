text = input("Enter text: ").upper().replace(" ", "")
choice = int(input("1 Encrypt 2 Decrypt: "))

col = 4

if choice == 1:
    while len(text) % col != 0:
        text += "X"

    rows = len(text) // col
    mat = []

    k = 0
    for i in range(rows):
        row = []
        for j in range(col):
            row.append(text[k])
            k += 1
        mat.append(row)

    res = ""
    for j in range(col):
        for i in range(rows):
            res += mat[i][j]

    print(res)

else:
    rows = len(text) // col
    mat = [[""] * col for _ in range(rows)]

    k = 0
    for j in range(col):
        for i in range(rows):
            mat[i][j] = text[k]
            k += 1

    res = ""
    for i in range(rows):
        for j in range(col):
            res += mat[i][j]

    print(res)
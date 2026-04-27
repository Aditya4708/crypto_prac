m = [
['M','O','N','A','R'],
['C','H','Y','B','D'],
['E','F','G','I','K'],
['L','P','Q','S','T'],
['U','V','W','X','Z']
]

text = input("Enter 2 letters: ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))

a = text[0]
b = text[1]

for i in range(5):
    for j in range(5):
        if m[i][j] == a:
            r1,c1 = i,j
        if m[i][j] == b:
            r2,c2 = i,j

if r1 == r2:
    if choice == 1:
        print(m[r1][(c1+1)%5] + m[r2][(c2+1)%5])
    else:
        print(m[r1][(c1-1)%5] + m[r2][(c2-1)%5])

elif c1 == c2:
    if choice == 1:
        print(m[(r1+1)%5][c1] + m[(r2+1)%5][c2])
    else:
        print(m[(r1-1)%5][c1] + m[(r2-1)%5][c2])

else:
    print("Not same row/column")
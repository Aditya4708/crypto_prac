# Playfair Cipher — `playfair.py`

## 📖 Topic Brief
The **Playfair Cipher** is a digraph substitution cipher — it encrypts **two letters at a time** (pairs/bigrams), unlike monoalphabetic ciphers that encrypt one. It uses a **5×5 matrix** generated from a keyword. Since the English alphabet has 26 letters but the matrix has only 25 cells, I and J are typically merged.

Invented by **Charles Wheatstone** in 1854 and popularized by **Lord Playfair**. Used by the British in WWI and WWII.

**Type:** Symmetric, Polygraphic Substitution Cipher

---

## 🔍 Line-by-Line Explanation

```python
m = [
['M','O','N','A','R'],
['C','H','Y','B','D'],
['E','F','G','I','K'],
['L','P','Q','S','T'],
['U','V','W','X','Z']
]
```
- The 5×5 **Playfair matrix** built from the keyword **"MONARCHY"**.
- Construction: Write the keyword first (removing duplicates), then fill remaining letters of the alphabet (I/J combined).
- Matrix positions: M(0,0), O(0,1), N(0,2), A(0,3), R(0,4), C(1,0), H(1,1), ...

```python
text = input("Enter 2 letters: ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- Takes exactly 2 letters as input. `1` = Encrypt, `2` = Decrypt.

```python
a = text[0]
b = text[1]
```
- Separates the two input letters.

```python
for i in range(5):
    for j in range(5):
        if m[i][j] == a:
            r1,c1 = i,j
        if m[i][j] == b:
            r2,c2 = i,j
```
- **Finds the row and column position** of each letter in the matrix.
- `r1, c1` = position of first letter. `r2, c2` = position of second letter.

```python
if r1 == r2:
    if choice == 1:
        print(m[r1][(c1+1)%5] + m[r2][(c2+1)%5])
    else:
        print(m[r1][(c1-1)%5] + m[r2][(c2-1)%5])
```
- **Same Row Rule:** Both letters in the same row.
  - **Encrypt:** Replace each letter with the one to its **right** (wrap around).
  - **Decrypt:** Replace each letter with the one to its **left** (wrap around).

```python
elif c1 == c2:
    if choice == 1:
        print(m[(r1+1)%5][c1] + m[(r2+1)%5][c2])
    else:
        print(m[(r1-1)%5][c1] + m[(r2-1)%5][c2])
```
- **Same Column Rule:** Both letters in the same column.
  - **Encrypt:** Replace each with the one **below** (wrap around).
  - **Decrypt:** Replace each with the one **above** (wrap around).

```python
else:
    print("Not same row/column")
```
- **Rectangle Rule:** If letters form a rectangle, swap columns (take the letter in the same row but the other letter's column).
  
> ⚠️ **Note:** This implementation only handles same-row and same-column cases. A complete Playfair cipher would also handle the rectangle case.

---

## 📝 Sample Input & Output

### Same Row Encryption
```
Enter 2 letters: MO
1 Encrypt 2 Decrypt: 1
Output: ON
```
**Explanation:** M is at (0,0), O is at (0,1). Same row → shift right: M→O, O→N.

### Same Column Encryption
```
Enter 2 letters: MU
1 Encrypt 2 Decrypt: 1
Output: CL  (hypothetical - M(0,0)→C(1,0), U(4,0)→M(0,0))
```

### Same Row Decryption
```
Enter 2 letters: ON
1 Encrypt 2 Decrypt: 2
Output: MO
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Frequency Analysis of Digraphs** | Analyze the frequency of letter pairs (bigrams) in the ciphertext and compare with known English bigram frequencies (TH, HE, IN, ER, etc.). |
| **Known Plaintext Attack** | If plaintext-ciphertext pairs are known, the matrix can be reconstructed. |
| **Brute Force** | 25! possible matrices ≈ 1.5 × 10²⁵ — computationally infeasible for brute force, but practical attacks exist via hill climbing. |
| **Pattern Analysis** | Since it encrypts pairs, repeated digraphs in plaintext produce repeated digraphs in ciphertext. |
| **Hill Climbing / Simulated Annealing** | Modern computational approach: start with a random key, score decryptions by English-likeness, and iteratively improve. |

**Verdict:** Stronger than monoalphabetic ciphers but breakable with computational methods. Was considered secure enough for military use in early 20th century.

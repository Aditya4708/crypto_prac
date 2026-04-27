# Columnar Transposition Cipher — `colcumnar.py`

## 📖 Topic Brief
The **Columnar Transposition Cipher** is a transposition cipher that rearranges the order of characters without changing them. The plaintext is written row by row into a grid of fixed columns, and the ciphertext is read out **column by column**.

Unlike substitution ciphers (which replace characters), transposition ciphers **shuffle the positions** of characters.

**Type:** Symmetric, Transposition Cipher

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper().replace(" ", "")
```
- Takes input, converts to uppercase, and **removes spaces** (spaces would reveal word boundaries).

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
col = 4
```
- Fixed number of columns = 4. This is the key (number of columns determines the rearrangement).

### Encryption Block:

```python
if choice == 1:
    while len(text) % col != 0:
        text += "X"
```
- **Padding:** Adds "X" characters to make the text length a multiple of 4 (so the grid is complete).

```python
    rows = len(text) // col
    mat = []
```
- Calculates number of rows. Creates empty matrix.

```python
    k = 0
    for i in range(rows):
        row = []
        for j in range(col):
            row.append(text[k])
            k += 1
        mat.append(row)
```
- **Fills the matrix row by row.**
- Example: "HELLOWORLD" with 4 columns:
  ```
  H E L L
  O W O R
  L D X X
  ```

```python
    res = ""
    for j in range(col):
        for i in range(rows):
            res += mat[i][j]
```
- **Reads the matrix column by column** to produce ciphertext.
- Column 0: H,O,L → Column 1: E,W,D → Column 2: L,O,X → Column 3: L,R,X
- Result: `HOLEWDLOXLRX`

```python
    print(res)
```
- Outputs the ciphertext.

### Decryption Block:

```python
else:
    rows = len(text) // col
    mat = [[""] * col for _ in range(rows)]
```
- Creates an empty matrix of the right size.

```python
    k = 0
    for j in range(col):
        for i in range(rows):
            mat[i][j] = text[k]
            k += 1
```
- **Fills the matrix column by column** (reverse of encryption — ciphertext was read column-wise).

```python
    res = ""
    for i in range(rows):
        for j in range(col):
            res += mat[i][j]
```
- **Reads row by row** to reconstruct the plaintext.

```python
    print(res)
```
- Outputs the decrypted text.

---

## 📝 Sample Input & Output

### Encryption
```
Enter text: HELLO WORLD
1 Encrypt 2 Decrypt: 1
```
Text after removing spaces: `HELLOWORLD`  
After padding: `HELLOWORLDXX`  
Grid (4 columns):
```
H E L L
O W O R
L D X X
```
Reading columns: H,O,L | E,W,D | L,O,X | L,R,X  
**Output: HOLEWDLOXLRX**

### Decryption
```
Enter text: HOLEWDLOXLRX
1 Encrypt 2 Decrypt: 2
Output: HELLOWORLDXX
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Brute Force on Column Count** | Try all possible column widths. For short messages, very few options exist. |
| **Anagramming** | Rearrange columns and look for recognizable patterns or English words. |
| **Frequency Analysis (limited)** | Letter frequencies are preserved (same letters, different order), so frequency analysis confirms it's a transposition cipher. |
| **Multiple Anagramming** | With multiple ciphertexts of the same key, align columns across messages to find the correct order. |
| **Known Plaintext Attack** | If any part of the plaintext is known, the column rearrangement pattern can be deduced. |
| **Bigram/Trigram Analysis** | Check if common letter pairs (TH, HE, IN) appear when columns are rearranged in different orders. |

**Verdict:** Moderate security. Much stronger when combined with substitution (forming a **product cipher**).

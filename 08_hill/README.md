# Hill Cipher — `hill.py`

## 📖 Topic Brief
The **Hill Cipher** is a polygraphic substitution cipher that uses **linear algebra (matrix multiplication)** to encrypt blocks of letters. It encrypts multiple letters at once using a key matrix. For a 2×2 key matrix, it encrypts 2 letters at a time.

Invented by **Lester S. Hill** in 1929. It's the first polygraphic cipher that was practical for more than 2 letters.

**Formula:**  
- Encryption: `C = K × P mod 26` (matrix multiplication)  
- Decryption: `P = K⁻¹ × C mod 26` (using inverse key matrix)  

**Type:** Symmetric, Polygraphic Substitution Cipher

---

## 🔍 Line-by-Line Explanation

```python
key = [[3,3],[2,5]]
inv = [[15,17],[20,9]]
```
- `key` = 2×2 encryption key matrix: `[[3,3],[2,5]]`
- `inv` = 2×2 **modular inverse** matrix of the key (mod 26).
- To verify: key × inv mod 26 should give the identity matrix `[[1,0],[0,1]]`.
- Verification: `[3×15+3×20, 3×17+3×9] = [105, 78]`, `105 mod 26 = 1`, `78 mod 26 = 0` ✓

```python
text = input("Enter text (even letters): ").upper()
```
- Input must have an **even number of letters** (since we encrypt 2 at a time).

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
use = key
if choice == 2:
    use = inv
```
- Uses the key matrix for encryption, the inverse matrix for decryption.

```python
result = ""
```
- Empty result string.

```python
for i in range(0, len(text), 2):
```
- Processes text in **pairs** (step=2): positions 0-1, 2-3, 4-5, etc.

```python
    a = ord(text[i]) - 65
    b = ord(text[i+1]) - 65
```
- Converts the two letters to numeric values (0–25).

```python
    x = (use[0][0]*a + use[0][1]*b) % 26
    y = (use[1][0]*a + use[1][1]*b) % 26
```
- **Matrix multiplication mod 26:**
  - `x = (row1 of matrix) · (column vector) mod 26`
  - `y = (row2 of matrix) · (column vector) mod 26`
  - This is: `[x, y] = [[m00,m01],[m10,m11]] × [a, b] mod 26`

```python
    result += chr(x + 65)
    result += chr(y + 65)
```
- Converts both results back to letters and appends.

```python
print(result)
```
- Prints the final result.

---

## 📝 Sample Input & Output

### Encryption
```
Enter text (even letters): HI
1 Encrypt 2 Decrypt: 1
```
**Calculation:**  
H=7, I=8  
x = (3×7 + 3×8) mod 26 = (21+24) mod 26 = 45 mod 26 = 19 → T  
y = (2×7 + 5×8) mod 26 = (14+40) mod 26 = 54 mod 26 = 2 → C  
**Output: TC**

### Decryption
```
Enter text (even letters): TC
1 Encrypt 2 Decrypt: 2
```
**Calculation:**  
T=19, C=2  
x = (15×19 + 17×2) mod 26 = (285+34) mod 26 = 319 mod 26 = 7 → H  
y = (20×19 + 9×2) mod 26 = (380+18) mod 26 = 398 mod 26 = 8 → I  
**Output: HI**

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Known Plaintext Attack** | If 2 plaintext-ciphertext pairs (4 letters each) are known, the key matrix can be solved using linear algebra. |
| **Frequency Analysis** | Less effective than on monoalphabetic ciphers but digraph frequency analysis can still help with larger ciphertexts. |
| **Determinant Attack** | The key matrix must have a determinant coprime with 26. This limits the number of valid keys. |
| **Brute Force** | For a 2×2 matrix: 26⁴ = 456,976 possibilities, but only ~37,000 are valid (invertible mod 26). Feasible for computers. |
| **Chosen Plaintext Attack** | Choose specific plaintexts to directly solve for the key matrix columns. |

**Verdict:** Stronger than monoalphabetic ciphers but vulnerable to known-plaintext attacks. Security increases with larger matrix sizes.

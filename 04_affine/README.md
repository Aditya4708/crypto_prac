# Affine Cipher — `affine.py`

## 📖 Topic Brief
The **Affine Cipher** combines the **multiplicative** and **additive** ciphers. It uses two keys: `a` (multiplicative) and `b` (additive). The key `a` must be coprime with 26.

**Formula:**  
- Encryption: `C = (a × P + b) mod 26`  
- Decryption: `P = a⁻¹ × (C - b) mod 26`  

Where a⁻¹ is the modular multiplicative inverse of `a` mod 26.

**Type:** Symmetric, Monoalphabetic Substitution Cipher  
**Key Space:** 12 × 26 = 312 possible key combinations

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper()
```
- Takes input text and converts to uppercase.

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
```
- `a` = multiplicative key (must be coprime with 26: 1,3,5,7,9,11,15,17,19,21,23,25).
- `b` = additive key (0–25).

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
ainv = -1
for i in range(26):
    if (a * i) % 26 == 1:
        ainv = i
```
- **Finds the modular inverse of `a`.**
- Brute-force searches i such that `(a × i) mod 26 = 1`.
- Example: a=5 → ainv=21, because `5×21 = 105`, `105 mod 26 = 1`.

```python
result = ""
```
- Initializes empty output string.

```python
for ch in text:
    if ch.isalpha():
        x = ord(ch) - 65
```
- Converts each alphabetic character to 0–25.

```python
        if choice == 1:
            y = (a * x + b) % 26
```
- **Encryption:** Applies `C = (a × P + b) mod 26`.

```python
        else:
            y = (ainv * (x - b)) % 26
```
- **Decryption:** Applies `P = a⁻¹ × (C - b) mod 26`.

```python
        result += chr(y + 65)
```
- Converts numeric result back to a letter.

```python
    else:
        result += ch
```
- Preserves non-letter characters.

```python
print(result)
```
- Prints the result.

---

## 📝 Sample Input & Output

### Encryption (a=5, b=8)
```
Enter text: HELLO
Enter a: 5
Enter b: 8
1 Encrypt 2 Decrypt: 1
Output: RCLLA
```
**Step-by-step:** H(7): (5×7+8) mod 26 = 43 mod 26 = 17 → R, E(4): (5×4+8)=28 mod 26=2 → C, L(11): (5×11+8)=63 mod 26=11 → L, O(14): (5×14+8)=78 mod 26=0 → A

### Decryption (a=5, b=8, a⁻¹=21)
```
Enter text: RCLLA
Enter a: 5
Enter b: 8
1 Encrypt 2 Decrypt: 2
Output: HELLO
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Brute Force** | 312 key combinations — feasible manually, trivial by computer. |
| **Frequency Analysis** | Still a monoalphabetic cipher, so frequency analysis breaks it easily. |
| **Known Plaintext Attack** | Two known plaintext-ciphertext pairs give two equations with two unknowns (a, b), solving the key instantly. |
| **Chosen Plaintext Attack** | Encrypt chosen letters to deduce `a` and `b` algebraically. |

**Verdict:** Slightly stronger than Caesar but still fundamentally weak due to monoalphabetic nature.

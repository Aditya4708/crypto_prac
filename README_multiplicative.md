# Multiplicative Cipher — `multiplicative.py`

## 📖 Topic Brief
The **Multiplicative Cipher** encrypts by multiplying each letter's numeric value by a key, modulo 26. The key must be **coprime with 26** (i.e., `gcd(key, 26) = 1`) for decryption to be possible. Valid keys: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

**Formula:**  
- Encryption: `C = (P × K) mod 26`  
- Decryption: `P = (C × K⁻¹) mod 26`  

Where K⁻¹ is the **modular multiplicative inverse** of K mod 26.

**Type:** Symmetric, Monoalphabetic Substitution Cipher  
**Key Space:** 12 valid keys

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper()
```
- Takes input and converts to uppercase.

```python
key = int(input("Enter key: "))
```
- The multiplicative key. Must be coprime with 26.

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
inv = -1
for i in range(26):
    if (key * i) % 26 == 1:
        inv = i
```
- **Finds the modular inverse** of the key.
- Tries all values 0–25. If `(key × i) mod 26 == 1`, then `i` is the inverse.
- Example: If key=3, then inv=9 because `3×9=27`, and `27 mod 26 = 1`.

```python
result = ""
```
- Empty result string.

```python
for ch in text:
    if ch.isalpha():
        x = ord(ch) - 65
```
- Converts each letter to its numeric value (A=0, B=1, ..., Z=25).

```python
        if choice == 1:
            y = (x * key) % 26
```
- **Encryption:** Multiplies by the key and takes mod 26.

```python
        else:
            y = (x * inv) % 26
```
- **Decryption:** Multiplies by the modular inverse of the key.

```python
        result += chr(y + 65)
```
- Converts the result back to a character.

```python
    else:
        result += ch
```
- Preserves non-alphabetic characters.

```python
print(result)
```
- Outputs the result.

---

## 📝 Sample Input & Output

### Encryption (key = 7)
```
Enter text: HELLO
Enter key: 7
1 Encrypt 2 Decrypt: 1
Output: XCZZY
```
**Step-by-step:** H(7)×7=49 mod 26=23→X, E(4)×7=28 mod 26=2→C, L(11)×7=77 mod 26=25→Z, L→Z, O(14)×7=98 mod 26=24→Y

### Decryption (key = 7, inverse = 15)
```
Enter text: XCZZY
Enter key: 7
1 Encrypt 2 Decrypt: 2
Output: HELLO
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Brute Force** | Only 12 valid keys — trivially breakable. |
| **Frequency Analysis** | Same letter always maps to the same ciphertext letter, so frequency analysis works. |
| **Known Plaintext Attack** | One known pair reveals the key: `K = C × P⁻¹ mod 26`. |

**Verdict:** Weak due to very small key space. Slightly stronger than additive but still easily broken.

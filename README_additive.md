# Additive Cipher — `additive.py`

## 📖 Topic Brief
The **Additive Cipher** is mathematically identical to the Shift/Caesar Cipher. Each letter is replaced by another letter that is a fixed number of positions ahead (encryption) or behind (decryption) in the alphabet.

**Formula:**  
- Encryption: `C = (P + K) mod 26`  
- Decryption: `P = (C - K) mod 26`  

Where P = plaintext letter (0–25), C = ciphertext letter, K = key.

**Type:** Symmetric, Monoalphabetic Substitution Cipher  
**Key Space:** 26 possible keys

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper()
```
- Takes plaintext/ciphertext input and converts to uppercase.

```python
key = int(input("Enter key: "))
```
- The additive key (shift amount). Must be between 0 and 25 for meaningful encryption.

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
result = ""
```
- Empty string to accumulate the output.

```python
for ch in text:
    if ch.isalpha():
```
- Iterates through each character; processes only alphabetic characters.

```python
        if choice == 1:
            result += chr((ord(ch) - 65 + key) % 26 + 65)
```
- **Encryption:** Converts char to 0–25, adds the key, wraps with mod 26, converts back.

```python
        else:
            result += chr((ord(ch) - 65 - key) % 26 + 65)
```
- **Decryption:** Subtracts the key instead of adding.

```python
    else:
        result += ch
```
- Non-alphabetic characters are preserved unchanged.

```python
print(result)
```
- Displays the result.

---

## 📝 Sample Input & Output

### Encryption
```
Enter text: ATTACK AT DAWN
Enter key: 5
1 Encrypt 2 Decrypt: 1
Output: FYYFHP FY IFBS
```
**Step-by-step:** A(0)+5=F(5), T(19)+5=Y(24), T→Y, A→F, C(2)+5=H(7), K(10)+5=P(15)...

### Decryption
```
Enter text: FYYFHP FY IFBS
Enter key: 5
1 Encrypt 2 Decrypt: 2
Output: ATTACK AT DAWN
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Brute Force** | Only 26 keys — trivially breakable by trying all shifts. |
| **Frequency Analysis** | Analyze letter frequencies in the ciphertext and compare with known English letter frequencies (E=12.7%, T=9.1%, etc.). |
| **Known Plaintext Attack** | A single known plaintext-ciphertext letter pair reveals the key: `K = C - P mod 26`. |
| **Ciphertext-Only Attack** | Even without any known plaintext, frequency analysis alone can break it. |

**Verdict:** Very weak cipher. Useful only for learning, not for actual security.

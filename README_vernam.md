# Vernam Cipher (One-Time Pad) — `vernam.py`

## 📖 Topic Brief
The **Vernam Cipher** (One-Time Pad) is theoretically the **only unbreakable cipher** when used correctly. Each letter of the plaintext is combined with a corresponding letter from a **random key of the same length**. The key must be:
1. As long as the message
2. Truly random
3. Used only once
4. Kept completely secret

**Formula:**  
- Encryption: `C = (P + K) mod 26`  
- Decryption: `P = (C - K) mod 26`  

**Type:** Symmetric, Polyalphabetic Substitution Cipher  
**Security:** Perfectly secure (if used correctly)

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper()
key = input("Enter key same length: ").upper()
```
- Takes the text and a key of the **same length** as the text. Both converted to uppercase.

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
result = ""
```
- Empty string for the result.

```python
for i in range(len(text)):
```
- Loops through each character position (index-based, since we need to match text[i] with key[i]).

```python
    a = ord(text[i]) - 65
    b = ord(key[i]) - 65
```
- `a` = numeric value of the current text letter.
- `b` = numeric value of the corresponding key letter.

```python
    if choice == 1:
        c = (a + b) % 26
    else:
        c = (a - b) % 26
```
- **Encrypt:** Add plaintext and key values mod 26.
- **Decrypt:** Subtract key value from ciphertext mod 26.

```python
    result += chr(c + 65)
```
- Converts numeric result back to a letter and appends.

```python
print(result)
```
- Prints the encrypted or decrypted text.

---

## 📝 Sample Input & Output

### Encryption
```
Enter text: HELLO
Enter key same length: XMCKL
1 Encrypt 2 Decrypt: 1
Output: EQNVZ
```
**Step-by-step:**
| Plain | H(7)  | E(4)  | L(11) | L(11) | O(14) |
|-------|-------|-------|-------|-------|-------|
| Key   | X(23) | M(12) | C(2)  | K(10) | L(11) |
| Sum   | 30    | 16    | 13    | 21    | 25    |
| mod26 | 4     | 16    | 13    | 21    | 25    |
| Cipher| E     | Q     | N     | V     | Z     |

### Decryption
```
Enter text: EQNVZ
Enter key same length: XMCKL
1 Encrypt 2 Decrypt: 2
Output: HELLO
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Key Reuse Attack** | If the same key is used twice, XOR/subtract the two ciphertexts to eliminate the key and recover plaintext. **This is the biggest practical vulnerability.** |
| **Short Key Attack** | If the key is shorter than the message and is repeated, it degrades to Vigenère cipher (breakable). |
| **Key Distribution Problem** | Securely sharing a key as long as the message is a massive logistical challenge. |
| **Non-Random Key** | If the key has patterns (e.g., English words), it weakens the cipher. |

**Verdict:** **Theoretically unbreakable** if the key is truly random, as long as the message, and never reused. In practice, key management makes it impractical for most uses.

> ⚠️ **Note:** This implementation does NOT handle non-alphabetic characters. If the input has spaces, it will crash because `key[i]` may map to a space character.

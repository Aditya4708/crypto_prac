# Product Cipher — `productcipher.py`

## 📖 Topic Brief
A **Product Cipher** combines two or more simple ciphers to create a stronger cipher. This implementation combines:
1. **Substitution** (Caesar/Shift cipher with key=3)
2. **Transposition** (Reversing the string)

The idea is that substitution alone is weak (vulnerable to frequency analysis) and transposition alone is weak (letters are unchanged), but combining them makes the cipher significantly stronger. Modern ciphers like **DES and AES** are product ciphers that use many rounds of substitution and transposition (permutation).

**Type:** Symmetric, Product Cipher (Substitution + Transposition)

---

## 🔍 Line-by-Line Explanation

```python
choice = input("Enter E for Encryption or D for Decryption: ").upper()
```
- Asks user for encryption ('E') or decryption ('D').

```python
text = input("Enter text: ").upper()
```
- Takes the input text, converted to uppercase.

```python
shift = 3
```
- The substitution key (shift value). Same as Caesar cipher with key=3.

### Encryption (Substitution → Transposition):

```python
if choice == 'E':
    sub = ""
    for ch in text:
        if ch.isalpha():
            sub += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            sub += ch
```
- **Step 1 — Substitution:** Each letter is shifted forward by 3 positions (Caesar cipher).
- `ord(ch) - 65` → converts to 0–25.
- `+ shift` → shifts by 3.
- `% 26` → wraps around Z.
- Non-alphabetic characters are preserved.

```python
    cipher = sub[::-1]
```
- **Step 2 — Transposition:** Reverses the substituted string.
- `[::-1]` is Python's string reversal.

```python
    print("After Substitution:", sub)
    print("Cipher Text:", cipher)
```
- Shows intermediate result (after substitution) and final ciphertext (after reversal).

### Decryption (Reverse Transposition → Reverse Substitution):

```python
elif choice == 'D':
    rev = text[::-1]
```
- **Step 1 — Undo Transposition:** Reverse the string first (undo the last step of encryption).

```python
    plain = ""
    for ch in rev:
        if ch.isalpha():
            plain += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            plain += ch
```
- **Step 2 — Undo Substitution:** Shift each letter backward by 3 (reverse Caesar).

```python
    print("After Reverse:", rev)
    print("Decrypted Text:", plain)
```
- Shows intermediate result and final plaintext.

```python
else:
    print("Invalid choice")
```
- Handles invalid input.

---

## 📝 Sample Input & Output

### Encryption
```
Enter E for Encryption or D for Decryption: E
Enter text: HELLO
```
**Step 1 - Substitution (shift 3):** H→K, E→H, L→O, L→O, O→R → `KHOOR`  
**Step 2 - Reversal:** KHOOR → `ROOHK`  
```
After Substitution: KHOOR
Cipher Text: ROOHK
```

### Decryption
```
Enter E for Encryption or D for Decryption: D
Enter text: ROOHK
```
**Step 1 - Reverse:** ROOHK → `KHOOR`  
**Step 2 - Reverse substitution (shift -3):** K→H, H→E, O→L, O→L, R→O → `HELLO`  
```
After Reverse: KHOOR
Decrypted Text: HELLO
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Brute Force** | Only 26 possible shift values, and the transposition is a simple reversal — trivially breakable. |
| **Known Structure Attack** | If the attacker knows it's substitution + reversal, they reverse the string and try 26 shifts. |
| **Frequency Analysis** | Reverse the ciphertext first, then apply standard frequency analysis on the resulting Caesar cipher. |
| **Known Plaintext Attack** | One known plaintext-ciphertext pair reveals the shift key immediately. |

**Verdict:** Slightly stronger than individual components but still very weak. The concept of product ciphers is important though — **AES uses 10+ rounds of substitution and permutation**, making it practically unbreakable.

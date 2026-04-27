# Shift Cipher (Caesar Cipher) — `shift.py`

## 📖 Topic Brief
The **Shift Cipher** (also called **Caesar Cipher**) is one of the oldest and simplest encryption techniques. It was used by Julius Caesar to communicate with his generals. Each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

**Type:** Symmetric, Substitution Cipher  
**Key Space:** 26 possible keys (0–25)

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper()
```
- Takes user input and converts it to uppercase so we only deal with A–Z (ASCII 65–90).

```python
key = int(input("Enter key: "))
```
- Takes the shift value (key). For example, key=3 means shift each letter by 3 positions.

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- User chooses: `1` for encryption, `2` for decryption.

```python
result = ""
```
- Initializes an empty string to store the encrypted/decrypted result.

```python
for ch in text:
```
- Loops through each character of the input text.

```python
    if ch.isalpha():
```
- Checks if the character is a letter (skips spaces, numbers, symbols).

```python
        if choice == 1:
            result += chr((ord(ch) - 65 + key) % 26 + 65)
```
- **Encryption formula:** `E(x) = (x + key) mod 26`
- `ord(ch) - 65` → Converts letter to 0–25 (A=0, B=1, ..., Z=25).
- `+ key` → Shifts the letter forward by the key.
- `% 26` → Wraps around if it goes past Z.
- `+ 65` → Converts back to ASCII.
- `chr(...)` → Converts ASCII number back to a character.

```python
        else:
            result += chr((ord(ch) - 65 - key) % 26 + 65)
```
- **Decryption formula:** `D(x) = (x - key) mod 26`
- Same logic, but shifts backward.

```python
    else:
        result += ch
```
- If the character is not a letter (e.g., space, number), keep it as-is.

```python
print(result)
```
- Prints the final encrypted or decrypted text.

---

## 📝 Sample Input & Output

### Encryption
```
Enter text: HELLO WORLD
Enter key: 3
1 Encrypt 2 Decrypt: 1
Output: KHOOR ZRUOG
```
**Explanation:** H→K, E→H, L→O, L→O, O→R, W→Z, O→R, R→U, L→O, D→G

### Decryption
```
Enter text: KHOOR ZRUOG
Enter key: 3
1 Encrypt 2 Decrypt: 2
Output: HELLO WORLD
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Brute Force** | Only 26 possible keys, so an attacker can try all 26 shifts and find the plaintext easily. |
| **Frequency Analysis** | In English, 'E' is the most common letter. The attacker finds the most frequent letter in ciphertext and calculates the shift. |
| **Known Plaintext Attack** | If the attacker knows even one plaintext-ciphertext pair, the key is immediately revealed. |

**Verdict:** Extremely weak. Never use for real security.

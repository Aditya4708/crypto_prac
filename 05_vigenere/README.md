# Vigenère Cipher — `vigenere.py`

## 📖 Topic Brief
The **Vigenère Cipher** is a polyalphabetic substitution cipher that uses a **keyword** to shift letters by varying amounts. Unlike Caesar cipher (which uses one shift), each letter of the key specifies a different shift. This makes it much harder to break with simple frequency analysis.

It was considered "unbreakable" for 300 years and was called **"le chiffre indéchiffrable"** (the indecipherable cipher).

**Formula:**  
- Encryption: `Cᵢ = (Pᵢ + Kᵢ) mod 26`  
- Decryption: `Pᵢ = (Cᵢ - Kᵢ) mod 26`  

Where Kᵢ = key letter at position `i mod key_length`.

**Type:** Symmetric, Polyalphabetic Substitution Cipher

---

## 🔍 Line-by-Line Explanation

```python
text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
```
- Takes plaintext/ciphertext and keyword, both converted to uppercase.

```python
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- `1` = Encrypt, `2` = Decrypt.

```python
result = ""
j = 0
```
- `result` stores the output. `j` tracks which key letter to use next (increments only for alphabetic characters).

```python
for ch in text:
    if ch.isalpha():
```
- Iterates through each character; processes only letters.

```python
        a = ord(ch) - 65
        b = ord(key[j % len(key)]) - 65
```
- `a` = numeric value of the current text character (0–25).
- `b` = numeric value of the current key character. `j % len(key)` wraps the key around if it's shorter than the text.

```python
        if choice == 1:
            c = (a + b) % 26
        else:
            c = (a - b) % 26
```
- **Encrypt:** Add the key shift. **Decrypt:** Subtract the key shift.

```python
        result += chr(c + 65)
        j += 1
```
- Converts back to a letter and appends to result. Advances the key position.

```python
    else:
        result += ch
```
- Non-alphabetic characters are kept unchanged (and `j` does NOT increment, so the key alignment is preserved).

```python
print(result)
```
- Prints the result.

---

## 📝 Sample Input & Output

### Encryption (key = "KEY")
```
Enter text: HELLO WORLD
Enter key: KEY
1 Encrypt 2 Decrypt: 1
Output: RIJVS UYVJN
```
**Step-by-step:**
| Plain | H | E | L | L | O | W | O | R | L | D |
|-------|---|---|---|---|---|---|---|---|---|---|
| Key   | K | E | Y | K | E | K | E | Y | K | E |
| Shift | 10| 4 |24 |10 | 4 |10 | 4 |24 |10 | 4 |
| Cipher| R | I | J | V | S | U | Y | V | J | N |

### Decryption
```
Enter text: RIJVS UYVJN
Enter key: KEY
1 Encrypt 2 Decrypt: 2
Output: HELLO WORLD
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Kasiski Examination** | Find repeated sequences in ciphertext to determine key length, then break each "column" as a Caesar cipher. |
| **Friedman Test (Index of Coincidence)** | Statistical method to estimate key length by measuring how "flat" the letter distribution is. |
| **Frequency Analysis (after finding key length)** | Once key length is known, each column is a simple Caesar cipher and can be broken individually. |
| **Known Plaintext Attack** | If part of the plaintext is known, the key can be recovered: `K = C - P mod 26`. |
| **Dictionary Attack** | If the key is an English word, try common words as keys. |

**Verdict:** Much stronger than monoalphabetic ciphers but broken by Kasiski/Friedman methods. Not secure by modern standards.

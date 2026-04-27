# Rail Fence / Transposition Cipher — `transposition.py`

## 📖 Topic Brief
This is a **simple transposition cipher** that rearranges characters by separating them into **even-positioned** and **odd-positioned** characters, then concatenating them. It's a form of the **Rail Fence Cipher** with 2 rails.

Characters at even positions (2nd, 4th, 6th...) are grouped together, followed by characters at odd positions (1st, 3rd, 5th...). This shuffles the text without changing any letters.

**Type:** Symmetric, Transposition Cipher

---

## 🔍 Line-by-Line Explanation

### Encryption:

```python
text = input("Enter text: ").upper()
choice = int(input("1 Encrypt 2 Decrypt: "))
```
- Takes input text and choice.

```python
if choice == 1:
    even = ""
    odd = ""
```
- Two strings: `even` for characters at even positions (2nd, 4th...), `odd` for odd positions (1st, 3rd...).

```python
    for i in range(len(text)):
        if (i + 1) % 2 == 0:
            even += text[i]
        else:
            odd += text[i]
```
- `i+1` converts from 0-indexed to 1-indexed position.
- If position is even (2nd, 4th, 6th...) → goes to `even`.
- If position is odd (1st, 3rd, 5th...) → goes to `odd`.
- Example "HELLO": H(1st→odd), E(2nd→even), L(3rd→odd), L(4th→even), O(5th→odd)

```python
    print(even + odd)
```
- Concatenates: even-positioned characters first, then odd-positioned.
- "HELLO" → even="EL" + odd="HLO" = **"ELHLO"**

### Decryption:

```python
else:
    n = len(text)
    e = n // 2
    o = n - e
```
- `e` = number of even-positioned characters = `n // 2`.
- `o` = number of odd-positioned characters = `n - e`.

```python
    even = text[:e]
    odd = text[e:]
```
- Splits ciphertext: first `e` characters are the even group, remaining are the odd group.

```python
    res = ""
    x = y = 0
```
- `x` tracks position in `even`, `y` tracks position in `odd`.

```python
    for i in range(n):
        if (i + 1) % 2 == 0:
            res += even[x]
            x += 1
        else:
            res += odd[y]
            y += 1
```
- Reconstructs original order by interleaving: odd positions pull from `odd`, even positions pull from `even`.

```python
    print(res)
```
- Prints the decrypted text.

---

## 📝 Sample Input & Output

### Encryption
```
Enter text: HELLO WORLD
1 Encrypt 2 Decrypt: 1
```
Positions (1-indexed):
```
H(1-odd) E(2-even) L(3-odd) L(4-even) O(5-odd) (6-even) W(7-odd) O(8-even) R(9-odd) L(10-even) D(11-odd)
```
Even = "EL OL" → Odd = "HLO WRD"  
**Output: EL OLHLO WRD**

### Decryption
```
Enter text: EL OLHLO WRD
1 Encrypt 2 Decrypt: 2
Output: HELLO WORLD
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Pattern Recognition** | Only 2 possible rearrangements (even-odd or odd-even). Trivially reversible. |
| **Brute Force** | With only 1 possible key (the even/odd split), there's nothing to brute force. |
| **Frequency Analysis** | Letter frequencies are unchanged — confirms it's a transposition cipher. |
| **Known Plaintext** | Any known word immediately reveals the pattern. |

**Verdict:** Extremely weak on its own. Only useful as a building block within a product cipher.

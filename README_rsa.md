# RSA Encryption — `rsa.py`

## 📖 Topic Brief
**RSA (Rivest–Shamir–Adleman)** is the most widely used **asymmetric (public-key) encryption** algorithm. Unlike symmetric ciphers where both parties share the same key, RSA uses a **key pair**:
- **Public Key (e, n):** Shared openly — used to encrypt.
- **Private Key (d, n):** Kept secret — used to decrypt.

**Mathematical Foundation:**
1. Choose two primes `p` and `q`
2. Compute `n = p × q`
3. Compute `φ(n) = (p-1)(q-1)` (Euler's totient)
4. Choose `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`
5. Find `d` such that `(d × e) mod φ(n) = 1` (modular inverse)
6. **Encrypt:** `C = M^e mod n`
7. **Decrypt:** `M = C^d mod n`

**Type:** Asymmetric (Public Key) Cryptosystem

---

## 🔍 Line-by-Line Explanation

```python
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
```
- Two prime numbers. Example: p=61, q=53. In real RSA, these are hundreds of digits long.

```python
n = p * q
phi = (p-1) * (q-1)
```
- `n` = modulus, used in both public and private keys.
- `phi` = Euler's totient `φ(n) = (p-1)(q-1)`. This is the secret that enables key generation.

```python
e = int(input("Enter e: "))
```
- The public exponent. Must satisfy: `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
- Common values: 3, 17, 65537. (65537 is standard in practice.)

```python
d = 0
for i in range(1, phi):
    if (i * e) % phi == 1:
        d = i
        break
```
- **Finds the private key `d`** — the modular multiplicative inverse of `e` mod `φ(n)`.
- Searches for `d` such that `(d × e) mod φ(n) = 1`.
- In practice, the **Extended Euclidean Algorithm** is used (much faster).

```python
msg = int(input("Enter message (number): "))
```
- The message to encrypt (as a number). Must be less than `n`.

```python
c = (msg ** e) % n
```
- **Encryption:** `C = M^e mod n`. Raises message to the power `e`, modulo `n`.

```python
m = (c ** d) % n
```
- **Decryption:** `M = C^d mod n`. Raises ciphertext to the power `d`, modulo `n`.

```python
print("Public Key (e,n):", (e, n))
print("Private Key (d,n):", (d, n))
print("Encrypted:", c)
print("Decrypted:", m)
```
- Displays the public key, private key, encrypted message, and decrypted message.
- The decrypted message should match the original message.

---

## 📝 Sample Input & Output

```
Enter prime p: 61
Enter prime q: 53
Enter e: 17
Enter message (number): 65
```

**Calculations:**
- n = 61 × 53 = 3233
- φ(n) = 60 × 52 = 3120
- d: find d where (d × 17) mod 3120 = 1 → d = 2753
- Encryption: 65^17 mod 3233 = 2790
- Decryption: 2790^2753 mod 3233 = 65 ✓

```
Public Key (e,n): (17, 3233)
Private Key (d,n): (2753, 3233)
Encrypted: 2790
Decrypted: 65
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Factoring Attack** | If an attacker factors `n` into `p` and `q`, they can compute `φ(n)` and derive `d`. This is the main attack vector. |
| **Small Key Attack** | If `p`, `q`, or `n` are too small, factoring is trivial. Use at least 2048-bit keys. |
| **Wiener's Attack** | If the private key `d` is too small (relative to `n`), it can be recovered using continued fractions. |
| **Common Modulus Attack** | If two users share the same `n` but different `e` values, the plaintext can be recovered. |
| **Low Public Exponent Attack** | If `e` is very small (e.g., e=3) and the message is short, the ciphertext might not wrap around mod n, making decryption trivial. |
| **Timing Attack** | Measuring how long decryption takes can leak information about the private key. Prevented with constant-time implementations. |
| **Chosen Ciphertext Attack** | An attacker sends specially crafted ciphertexts and analyzes the responses to extract the private key. Prevented with padding schemes (OAEP). |
| **Quantum Computing (Shor's Algorithm)** | Can factor large numbers efficiently, breaking RSA. Not yet practical but a future threat. |

### RSA Key Size Recommendations (2024+)
| Key Size | Security Level |
|----------|---------------|
| 1024-bit | ❌ Broken / Insecure |
| 2048-bit | ✅ Minimum recommended |
| 3072-bit | ✅ Good for long-term security |
| 4096-bit | ✅ High security |

**Verdict:** RSA is a cornerstone of modern cryptography (HTTPS, digital signatures, etc.). Secure when implemented correctly with large keys and proper padding (PKCS#1 v2.0 / OAEP).

> ⚠️ **Note:** This implementation uses Python's `**` operator for exponentiation, which is very slow for large numbers. Real implementations use **modular exponentiation** (`pow(msg, e, n)`) which is much faster.

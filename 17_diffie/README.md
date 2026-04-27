# Diffie-Hellman Key Exchange — `diffie.py`

## 📖 Topic Brief
**Diffie-Hellman (DH)** is a method for two parties to establish a **shared secret key** over an insecure channel, without ever transmitting the key itself. Invented by **Whitfield Diffie and Martin Hellman** in 1976, it was the first practical key exchange protocol.

It relies on the **Discrete Logarithm Problem** — given `g^a mod p`, it's computationally hard to find `a`.

**How it works:**
1. Both parties agree on public values: prime `p` and generator `g`
2. Each party picks a private key and computes a public key
3. They exchange public keys
4. Each computes the **same shared secret** using their private key + the other's public key

**Type:** Asymmetric Key Exchange Protocol

---

## 🔍 Line-by-Line Explanation

```python
p = 23   # prime number
g = 5    # generator
```
- `p` = a publicly known prime number (modulus).
- `g` = a publicly known generator (primitive root of `p`).
- In real DH, `p` is a very large prime (2048+ bits).

```python
a = int(input("Enter private key of User1: "))
b = int(input("Enter private key of User2: "))
```
- `a` = User1's **private key** (kept secret, never shared).
- `b` = User2's **private key** (kept secret, never shared).

```python
A = pow(g, a, p)
B = pow(g, b, p)
```
- `A = g^a mod p` → User1's **public key** (sent to User2 over the insecure channel).
- `B = g^b mod p` → User2's **public key** (sent to User1 over the insecure channel).
- `pow(g, a, p)` is Python's efficient modular exponentiation.

```python
k1 = pow(B, a, p)
k2 = pow(A, b, p)
```
- `k1 = B^a mod p` → User1 computes the shared secret using User2's public key + own private key.
- `k2 = A^b mod p` → User2 computes the shared secret using User1's public key + own private key.
- **Mathematically:** `k1 = (g^b)^a mod p = g^(ab) mod p = (g^a)^b mod p = k2` → **Both get the same key!**

```python
print("Public key of User1:", A)
print("Public key of User2:", B)
print("Secret key for User1:", k1)
print("Secret key for User2:", k2)
```
- Displays the public keys (can be seen by anyone) and the shared secret (same for both users).

---

## 📝 Sample Input & Output

```
Enter private key of User1: 6
Enter private key of User2: 15
Public key of User1: 8
Public key of User2: 19
Secret key for User1: 2
Secret key for User2: 2
```

**Step-by-step (p=23, g=5):**
- A = 5^6 mod 23 = 15625 mod 23 = **8**
- B = 5^15 mod 23 = ... mod 23 = **19**
- k1 = 19^6 mod 23 = **2**
- k2 = 8^15 mod 23 = **2** ✓ (Both match!)

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Man-in-the-Middle (MITM)** | An attacker intercepts both public keys and substitutes their own, establishing separate shared secrets with each party. **DH alone does NOT authenticate parties.** |
| **Discrete Logarithm Attack** | If an attacker can solve `g^a mod p = A` for `a`, the key is broken. Currently infeasible for large primes. |
| **Small Prime / Weak Generator** | If `p` is small or `g` is not a proper generator, the key space shrinks dramatically. |
| **Logjam Attack** | Exploits servers using 512-bit or 1024-bit DH parameters. Use 2048-bit minimum. |
| **Quantum Computing** | Shor's algorithm can solve discrete logarithms efficiently, breaking DH. |

### Prevention
- Use **authenticated DH** (e.g., with digital signatures or certificates) to prevent MITM.
- Use primes of at least **2048 bits**.

**Verdict:** DH is foundational to modern cryptography (used in TLS/HTTPS, VPNs, SSH). Must always be combined with authentication.

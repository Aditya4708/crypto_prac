# Euler's Totient Function — `toient.py`

## 📖 Topic Brief
**Euler's Totient Function** `φ(n)` counts the number of integers from 1 to n that are **relatively prime** (coprime) to n — meaning their GCD with n is 1.

This function is fundamental to **RSA encryption**, where:
- `φ(n) = (p-1)(q-1)` for `n = p × q` (product of two primes)
- The totient is used to compute the private key

**Key Properties:**
- If `n` is prime: `φ(n) = n - 1` (all numbers less than a prime are coprime to it)
- If `n = p × q` and `gcd(p,q) = 1`: `φ(n) = φ(p) × φ(q) = (p-1)(q-1)`

---

## 🔍 Line-by-Line Explanation

```python
import math
```
- Imports the `math` module for the `gcd()` function (Greatest Common Divisor).

```python
n = int(input("Enter number: "))
```
- Takes a positive integer input.

```python
if n == 1:
    print("Totient =", 0)
```
- **Special case:** `φ(1) = 0` — there are no numbers less than 1 that are coprime to 1. (By convention, some sources say φ(1)=1, but 0 is used here.)

```python
elif n > 1:
    prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
```
- **Primality test:** Checks if `n` is prime by testing divisibility from 2 to √n.
- `n**0.5` = square root of n. We only need to check up to √n because if n has a factor larger than √n, it must also have one smaller.
- If any `i` divides `n`, it's not prime.

```python
    if prime:
        print("Totient =", n - 1)
```
- **If n is prime:** `φ(n) = n - 1`. Every number from 1 to n-1 is coprime to a prime.
- Example: φ(7) = 6 → {1,2,3,4,5,6} are all coprime with 7.

```python
    else:
        m = int(input("Enter first number: "))
        x = int(input("Enter second number: "))
```
- **If n is NOT prime:** Asks user to input two factors of n.

```python
        if math.gcd(m, x) == 1:
            print("Totient =", (m - 1) * (x - 1))
        else:
            print("Numbers are not relatively prime")
```
- **Multiplicative property:** If `gcd(m, x) = 1` (they're coprime), then `φ(m × x) = (m-1)(x-1)`.
- This is the key formula used in RSA: if p and q are primes, `φ(pq) = (p-1)(q-1)`.
- If the two numbers are NOT coprime, this formula doesn't apply.

---

## 📝 Sample Input & Output

### Case 1: n is Prime
```
Enter number: 13
Totient = 12
```
**Explanation:** 13 is prime, so φ(13) = 13 - 1 = 12.

### Case 2: n is a Product of Two Primes (RSA-style)
```
Enter number: 15
Enter first number: 3
Enter second number: 5
Totient = 8
```
**Explanation:** 15 = 3 × 5. gcd(3,5)=1. φ(15) = (3-1)(5-1) = 2×4 = 8.  
**Verification:** Numbers coprime to 15 from 1-15: {1,2,4,7,8,11,13,14} = 8 numbers ✓

### Case 3: Numbers not coprime
```
Enter number: 12
Enter first number: 4
Enter second number: 6
Numbers are not relatively prime
```
**Explanation:** gcd(4,6) = 2 ≠ 1, so the formula doesn't apply.

---

## ⚠️ Possible Attacks (on RSA using Totient)

| Attack | Description |
|--------|-------------|
| **Factoring n** | If an attacker can factor `n` into `p` and `q`, they can compute `φ(n) = (p-1)(q-1)` and derive the private key. This is the fundamental hardness assumption of RSA. |
| **Pollard's rho / p-1 Attack** | Efficient factoring algorithms for numbers with small prime factors. |
| **General Number Field Sieve (GNFS)** | The most efficient known algorithm for factoring large numbers. Makes RSA keys < 1024 bits insecure. |
| **Quantum Computing (Shor's Algorithm)** | Can factor large numbers in polynomial time, breaking RSA entirely. Not yet practical at scale. |
| **Small Key Attack** | If p and q are too small or too close together, factoring becomes easy. |

**Verdict:** The security of RSA depends entirely on the difficulty of computing φ(n) without knowing the prime factors. Use RSA keys of at least **2048 bits** for current security.

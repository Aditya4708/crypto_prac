# MD5 vs SHA-1 Hashing Comparison — `md_sha1.py`

## 📖 Topic Brief
**MD5** and **SHA-1** are cryptographic hash functions that convert any input into a fixed-length hash value. They are used for data integrity verification, digital signatures, and password storage.

| Property | MD5 | SHA-1 |
|----------|-----|-------|
| **Output Size** | 128 bits (32 hex chars) | 160 bits (40 hex chars) |
| **Designed by** | Ronald Rivest (1991) | NSA (1995) |
| **Status** | ❌ Broken (collisions found) | ❌ Broken (collisions found in 2017) |
| **Speed** | Faster | Slightly slower |

This script hashes 1KB of data with both algorithms and compares their speed and output.

**Category:** Hashing / Data Integrity

---

## 🔍 Line-by-Line Explanation

```python
import hashlib
import time
```
- `hashlib` → provides MD5, SHA-1, SHA-256, and other hash functions.
- `time` → used to measure how long each hashing operation takes.

```python
data = "A" * 1024
```
- Creates a **1KB string** (1024 repetitions of the character "A") as test data.

```python
start = time.time()
md5_hash = hashlib.md5(data.encode()).hexdigest()
md5_time = time.time() - start
```
- **MD5 Hashing:**
  - `time.time()` → records the start time.
  - `data.encode()` → converts the string to bytes (required by hashlib).
  - `hashlib.md5(...)` → computes the MD5 hash.
  - `.hexdigest()` → returns the hash as a 32-character hex string.
  - `time.time() - start` → calculates the elapsed time in seconds.

```python
start = time.time()
sha1_hash = hashlib.sha1(data.encode()).hexdigest()
sha1_time = time.time() - start
```
- **SHA-1 Hashing:** Same process but using SHA-1 (produces a 40-character hex string).

```python
print("MD5 Hash :", md5_hash)
print("MD5 Time :", md5_time)
print("SHA1 Hash:", sha1_hash)
print("SHA1 Time:", sha1_time)
```
- Displays both hashes and their computation times for comparison.

---

## 📝 Sample Input & Output

```
MD5 Hash : a0396a5a8adc7e5fc7a28f1d2d3e4e5f   (32 hex characters)
MD5 Time : 0.000015 seconds

SHA1 Hash: 6f9b9af3cd6e8b8a73c2cdaad0641a3c5f4e7d23   (40 hex characters)
SHA1 Time: 0.000018 seconds
```

> Note: Actual hash values and times will vary. Times are typically in microseconds for 1KB of data.

---

## ⚠️ Possible Attacks

### MD5 Attacks
| Attack | Description |
|--------|-------------|
| **Collision Attack** | Two different inputs producing the same MD5 hash. First demonstrated in 2004 by Xiaoyun Wang. Can be done in seconds on modern hardware. |
| **Preimage Attack** | Given a hash, finding an input that produces it. Partially broken for MD5. |
| **Rainbow Table Attack** | Precomputed hash tables for common inputs. Effective because MD5 is fast. |
| **Length Extension Attack** | Appending data to a message without knowing the original, while computing a valid hash. |

### SHA-1 Attacks
| Attack | Description |
|--------|-------------|
| **SHAttered Attack (2017)** | Google and CWI Amsterdam produced the first SHA-1 collision — two different PDFs with the same SHA-1 hash. Cost ~$110,000 in cloud computing. |
| **Collision Attack** | Now feasible with sufficient computing resources. |
| **Birthday Attack** | A generic attack that finds collisions in O(2^(n/2)) operations. For SHA-1: 2^80 operations (feasible for well-funded attackers). |

### Comparison & Recommendations

| Algorithm | Collision Resistance | Use Today? | Alternative |
|-----------|---------------------|-----------|-------------|
| **MD5** | ❌ Completely broken | ❌ Never for security | SHA-256 |
| **SHA-1** | ❌ Broken (2017) | ❌ Deprecated | SHA-256 |
| **SHA-256** | ✅ Secure | ✅ Recommended | — |
| **SHA-3** | ✅ Secure | ✅ Recommended | — |

**Verdict:** Both MD5 and SHA-1 are **broken and should NOT be used** for any security purpose. Use **SHA-256** or **SHA-3** instead. MD5/SHA-1 are still acceptable for non-security checksums (e.g., verifying file downloads).

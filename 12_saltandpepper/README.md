# Salt and Pepper Hashing — `saltandpeper.py`

## 📖 Topic Brief
**Salting and Peppering** are techniques used to strengthen password hashing and protect against common attacks like rainbow table lookups and dictionary attacks.

- **Hash:** A one-way function that converts a password into a fixed-length string. You cannot reverse it.
- **Salt:** A random string **stored alongside the hash** in the database. Each user gets a unique salt (in this demo, all users share one salt for simplicity).
- **Pepper:** A secret string stored **separately from the database** (e.g., in application config). It adds another layer so even if the database is leaked, passwords are still protected.

**Hash Algorithm Used:** SHA-256 (256-bit output, 64 hex characters)

---

## 🔍 Line-by-Line Explanation

```python
import hashlib
```
- Imports Python's `hashlib` library which provides SHA-256 and other hashing algorithms.

```python
salt = "S@lt!"
pepper = "P3pp3r#"
```
- **Salt:** A fixed string added to the password before hashing. In production, each user should have a unique random salt.
- **Pepper:** A secret string known only to the application. Stored in config, NOT in the database.

```python
users = {
"Aditya": "pass12458",
"Nambiar": "pass123",
"user": "aditya123"
}
```
- A dictionary of usernames and their plaintext passwords (simulating user registration).

```python
database = {}
```
- Empty dictionary to store username → hashed_password pairs (simulating a database).

```python
def hash_password(password):
    return hashlib.sha256((pepper + salt + password).encode()).hexdigest()
```
- **Hashing function:** Concatenates `pepper + salt + password`, encodes to bytes, then applies SHA-256.
- `.encode()` → converts string to bytes (required by hashlib).
- `.hexdigest()` → returns the hash as a 64-character hexadecimal string.
- The order `pepper + salt + password` ensures both the salt and pepper contribute to the hash.

```python
for user, pwd in users.items():
    database[user] = hash_password(pwd)
```
- Iterates through all users and stores their hashed passwords in the database.

```python
print("Stored Hashes with Pepper + Salt:", database)
```
- Displays the stored hashes (simulating what would be in a real database).

```python
# Login
user = input("Enter UserID: ")
pwd = input("Enter Password: ")
```
- Simulates a login form — user enters their credentials.

```python
if user in database and database[user] == hash_password(pwd):
    print("Login Successful")
else:
    print("Login Failed")
```
- **Authentication logic:**
  1. Check if the username exists in the database.
  2. Hash the entered password with the same salt and pepper.
  3. Compare the resulting hash with the stored hash.
  4. If they match → login success. Otherwise → login failed.
- **Note:** The actual password is NEVER compared directly. Only hashes are compared.

---

## 📝 Sample Input & Output

### Successful Login
```
Stored Hashes with Pepper + Salt: {'Aditya': 'a1b2c3...', 'Nambiar': 'd4e5f6...', 'user': 'g7h8i9...'}
Enter UserID: Aditya
Enter Password: pass12458
✅ Login Successful
```

### Failed Login (wrong password)
```
Enter UserID: Aditya
Enter Password: wrongpass
❌ Login Failed
```

### Failed Login (wrong username)
```
Enter UserID: hacker
Enter Password: pass123
❌ Login Failed
```

---

## ⚠️ Possible Attacks

| Attack | Description |
|--------|-------------|
| **Rainbow Table Attack** | Precomputed hash tables for common passwords. **Salt defeats this** because the same password produces different hashes with different salts. |
| **Dictionary Attack** | Try hashing common passwords. Salt slows this down, and pepper makes it impossible without the pepper value. |
| **Brute Force Attack** | Try every possible password combination. SHA-256 is fast, so specialized algorithms like **bcrypt/scrypt/Argon2** are preferred (they're intentionally slow). |
| **Database Breach** | If the database is leaked, the attacker gets hashes + salt. Without the pepper (stored separately), they still can't crack passwords efficiently. |
| **Pepper Discovery** | If the attacker also gains access to application code/config and finds the pepper, salt still protects against rainbow tables. |
| **Pass-the-Hash Attack** | If the hash itself is used for authentication without re-hashing, an attacker can use a stolen hash directly. |
| **Collision Attack** | Finding two inputs that produce the same SHA-256 hash. Currently computationally infeasible for SHA-256. |

### Why Salt AND Pepper?
| Component | Stored Where | Protects Against |
|-----------|-------------|-----------------|
| **Salt** | In database (alongside hash) | Rainbow tables, identical passwords having same hash |
| **Pepper** | In application config (separate from DB) | Database-only breaches |

**Verdict:** Good practice for password storage. For production, use **bcrypt, scrypt, or Argon2** instead of SHA-256, as they have built-in salting and are intentionally slow to resist brute force.

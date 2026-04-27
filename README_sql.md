# SQL Injection Demo — `sql.py`

## 📖 Topic Brief
**SQL Injection (SQLi)** is one of the most dangerous web application vulnerabilities (OWASP Top 10). It occurs when user input is directly embedded into SQL queries without sanitization, allowing attackers to manipulate the query logic.

This script demonstrates a **vulnerable login system** using SQLite, showing how an attacker can bypass authentication by injecting malicious SQL.

**Category:** Web Application Security / OWASP Top 10

---

## 🔍 Line-by-Line Explanation

```python
import sqlite3
```
- Imports SQLite3, a lightweight database engine built into Python.

```python
con = sqlite3.connect(":memory:")
cur = con.cursor()
```
- Creates an **in-memory database** (exists only while the program runs).
- `cursor()` creates a cursor object to execute SQL commands.

```python
cur.execute("CREATE TABLE users(username TEXT, password TEXT)")
```
- Creates a `users` table with two columns: `username` and `password`.

```python
cur.execute("INSERT INTO users VALUES('admin','1234')")
cur.execute("INSERT INTO users VALUES('user','pass')")
```
- Inserts two user records into the table.

```python
username = input("Enter username: ")
password = input("Enter password: ")
```
- Takes login credentials from the user. **This is where the vulnerability begins** — raw input goes directly into the query.

```python
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
```
- **⚠️ VULNERABLE QUERY:** Builds the SQL query by **string concatenation** with raw user input.
- Normal input: `username=admin, password=1234` → `SELECT * FROM users WHERE username='admin' AND password='1234'`
- **Malicious input:** `username=' OR '1'='1' --` → Query becomes: `SELECT * FROM users WHERE username='' OR '1'='1' --' AND password=''`
- The `'1'='1'` is always true, and `--` comments out the rest → **bypasses authentication!**

```python
print("Query:", query)
```
- Prints the actual query being executed (shows how injection works).

```python
cur.execute(query)
data = cur.fetchone()
```
- Executes the (potentially injected) query and fetches the first result.

```python
if data:
    print("Login Success")
else:
    print("Login Failed")
```
- If any row is returned → login succeeds. With injection, a row is always returned.

---

## 📝 Sample Input & Output

### Normal Login (Valid Credentials)
```
Enter username: admin
Enter password: 1234
Query: SELECT * FROM users WHERE username='admin' AND password='1234'
Login Success
```

### Failed Login (Wrong Password)
```
Enter username: admin
Enter password: wrong
Query: SELECT * FROM users WHERE username='admin' AND password='wrong'
Login Failed
```

### 🔴 SQL Injection Attack (Bypass Login)
```
Enter username: ' OR '1'='1' --
Enter password: anything
Query: SELECT * FROM users WHERE username='' OR '1'='1' --' AND password='anything'
Login Success
```
**Why it works:** `'1'='1'` is always TRUE. `--` comments out the password check. The query returns all rows.

### 🔴 Another Injection (Close quote trick)
```
Enter username: admin' --
Enter password: anything
Query: SELECT * FROM users WHERE username='admin' --' AND password='anything'
Login Success
```
**Why it works:** `--` comments out everything after `admin'`, so no password is checked.

---

## ⚠️ Possible Attacks

| Attack Type | Description | Example Input |
|-------------|-------------|---------------|
| **Authentication Bypass** | Login without valid credentials | `' OR '1'='1' --` |
| **Data Extraction (UNION)** | Read data from other tables | `' UNION SELECT username, password FROM users --` |
| **Database Destruction (DROP)** | Delete entire tables | `'; DROP TABLE users; --` |
| **Blind SQL Injection** | Extract data by asking true/false questions | `' AND (SELECT COUNT(*) FROM users) > 0 --` |
| **Time-Based Blind SQLi** | Use delays to infer data | `' OR IF(1=1, SLEEP(5), 0) --` |

---

## 🛡️ How to Prevent SQL Injection

| Prevention Method | Description |
|-------------------|-------------|
| **Parameterized Queries** | Use `?` placeholders: `cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))` |
| **ORM (Object-Relational Mapping)** | Use frameworks like SQLAlchemy, Django ORM that auto-escape inputs |
| **Input Validation** | Whitelist allowed characters, reject special SQL characters |
| **Stored Procedures** | Pre-compiled SQL on the server side |
| **Least Privilege** | Database user should have minimum required permissions |
| **WAF (Web Application Firewall)** | Detects and blocks common injection patterns |

**Verdict:** SQL Injection is one of the **most critical** vulnerabilities. Always use parameterized queries — NEVER concatenate user input into SQL strings.

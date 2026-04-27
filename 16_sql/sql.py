import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

# Create table
cur.execute("CREATE TABLE users(username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES('admin','1234')")
cur.execute("INSERT INTO users VALUES('user','pass')")

username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerable query
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

print("Query:", query)

cur.execute(query)
data = cur.fetchone()

if data:
    print("Login Success")
else:
    print("Login Failed")
import hashlib
salt = "S@lt!"
pepper = "P3pp3r#"
users = {
"Aditya": "pass12458",
"Nambiar": "pass123",
"user": "aditya123"
}
database = {}
def hash_password(password):
    return hashlib.sha256((pepper + salt + password).encode()).hexdigest()

for user, pwd in users.items():
    database[user] = hash_password(pwd)
print("Stored Hashes with Pepper + Salt:", database)
# Login
user = input("Enter UserID: ")
pwd = input("Enter Password: ")
if user in database and database[user] == hash_password(pwd):
    print("Login Successful")
else:
    print(" Login Failed")
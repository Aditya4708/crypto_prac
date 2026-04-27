import hashlib
import time

# create 1KB data
data = "A" * 1024

# MD5
start = time.time()
md5_hash = hashlib.md5(data.encode()).hexdigest()
md5_time = time.time() - start

# SHA-1
start = time.time()
sha1_hash = hashlib.sha1(data.encode()).hexdigest()
sha1_time = time.time() - start

print("MD5 Hash :", md5_hash)
print("MD5 Time :", md5_time)

print("SHA1 Hash:", sha1_hash)
print("SHA1 Time:", sha1_time)
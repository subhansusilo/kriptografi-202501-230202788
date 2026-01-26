import hashlib

target_hash = "482c811da5d5b4bc6d497ffa98491e38"

wordlist = [
    "admin",
    "123456",
    "password",
    "password123",
    "qwerty",
    "letmein"
]

for word in wordlist:
    hash_word = hashlib.md5(word.encode()).hexdigest()
    if hash_word == target_hash:
        print("Password ditemukan:", word)
        break
    else:
        print("Mencoba:", word)

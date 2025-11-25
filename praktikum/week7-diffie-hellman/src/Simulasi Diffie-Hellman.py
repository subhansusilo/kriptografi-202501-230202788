import random

# Parameter umum
p = 23
g = 5

# Private key Alice & Bob
a = random.randint(1, p-1)
b = random.randint(1, p-1)

# Public key Alice & Bob
A_real = pow(g, a, p)   # Seharusnya dikirim Alice
B_real = pow(g, b, p)   # Seharusnya dikirim Bob

# Eve membuat private key sendiri
e = random.randint(1, p-1)
E = pow(g, e, p)         # Public key Eve

print("=== KUNCI PUBLIC ASLI ===")
print("Alice A =", A_real)
print("Bob   B =", B_real)
print("Eve   E =", E)
print()

# MITM ATTACK:
# Eve mencegat public key dan menggantinya dengan miliknya sendiri
A_to_B = E      # Alice → Eve → Bob
B_to_A = E      # Bob → Eve → Alice

print("=== KUNCI YANG DITERIMA (SUDAH DIGANTI EVE) ===")
print("Bob menerima dari Alice (A') =", A_to_B)
print("Alice menerima dari Bob (B') =", B_to_A)
print()

# Alice hitung shared secret (dengan kunci palsu)
shared_Alice = pow(B_to_A, a, p)

# Bob hitung shared secret (dengan kunci palsu)
shared_Bob = pow(A_to_B, b, p)

# Eve bisa hitung dua shared secret berbeda:
shared_Eve_with_Alice = pow(A_real, e, p)
shared_Eve_with_Bob   = pow(B_real, e, p)

print("=== KUNCI BERSAMA ===")
print("Kunci Alice :", shared_Alice)
print("Kunci Bob   :", shared_Bob)
print("Kunci Eve dengan Alice :", shared_Eve_with_Alice)
print("Kunci Eve dengan Bob   :", shared_Eve_with_Bob)
print()

# Apakah Alice dan Bob memiliki kunci sama?
print("Apakah kunci Alice == Bob?", shared_Alice == shared_Bob)

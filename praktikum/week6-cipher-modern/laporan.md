# Laporan Praktikum Kriptografi
Minggu ke-: 06  
Topik: [Cipher Modern (DES, AES, RSA)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.


---

## 2. Dasar Teori
1. Data Encryption Standard (DES)
   
DES (Data Encryption Standard) adalah algoritma kriptografi simetris yang dikembangkan oleh IBM pada tahun 1970-an dan disetujui oleh NIST (National Institute of Standards and Technology) pada tahun 1977.
Artinya, kunci yang sama digunakan untuk enkripsi dan dekripsi data.

- Cara Kerja Singkat:

a. DES menggunakan blok data 64-bit dan kunci 56-bit.

b. Proses enkripsi dilakukan dengan 16 kali putaran (rounds), di mana setiap putaran menggunakan operasi permutasi dan substitusi berdasarkan tabel tertentu.

c. Prinsip utamanya: confusion (penyamaran) dan diffusion (penyebaran).

- Kelebihan:

a. Struktur sederhana dan mudah diimplementasikan.

b. Dulu dianggap sangat aman.

- Kelemahan:

a. Ukuran kunci kecil (56-bit) → mudah dipecahkan dengan brute force.

b. Kini tidak lagi aman, digantikan oleh AES


2. Advanced Encryption Standard (AES)

AES (Advanced Encryption Standard) adalah algoritma kriptografi simetris yang menggantikan DES pada tahun 2001

- Cara Kerja Singkat:

a. Menggunakan blok data 128-bit dan panjang kunci 128, 192, atau 256-bit.

b. Proses enkripsi terdiri dari beberapa rounds (10, 12, atau 14) tergantung panjang kunci.

c. Setiap round melakukan operasi:

    a.SubBytes (substitusi dengan tabel S-box)

    b.ShiftRows (pergeseran baris)

    c.MixColumns (pencampuran kolom)

    d.AddRoundKey (penambahan kunci putaran)

- Kelebihan:

a. Sangat aman (belum ada serangan praktis yang berhasil memecah AES).

b. Cepat dan efisien untuk perangkat keras maupun perangkat lunak.

c. Digunakan secara luas (Wi-Fi, HTTPS, VPN, dll).

- Kelemahan:

a. Karena simetris, distribusi kunci antar pihak masih menjadi masalah (perlu cara aman untuk berbagi kunci).

3. RSA (Rivest–Shamir–Adleman)

- RSA adalah algoritma kriptografi asimetris, yang menggunakan dua kunci berbeda:

a. Kunci publik (public key) → untuk enkripsi

b. Kunci privat (private key) → untuk dekripsi

- Kelebihan:

a. Aman untuk pertukaran kunci dan tanda tangan digital.

b. Tidak perlu berbagi kunci rahasia sebelumnya.

- Kelemahan:

a. Lambat dibanding algoritma simetris (seperti AES).

b. Membutuhkan bilangan prima yang sangat besar (2048 bit atau lebih) untuk tetap aman

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat file `Cipher Modern.py` di folder `praktikum/week6-cipher-modernsrc/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python Cipher Modern.py`.)

---

## 5. Source Code
Langkah 1 — Implementasi DES (Opsional, Simulasi)

    from Crypto.Cipher import DES
    from Crypto.Random import get_random_bytes
    
    key = get_random_bytes(8)  # kunci 64 bit (8 byte)
    cipher = DES.new(key, DES.MODE_ECB)
    
    plaintext = b"ABCDEFGH"
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    
    decipher = DES.new(key, DES.MODE_ECB)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)

Langkah 2 — Implementasi AES-128

    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    
    key = get_random_bytes(16)  # 128 bit key
    cipher = AES.new(key, AES.MODE_EAX)
    
    plaintext = b"Modern Cipher AES Example"
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    print("Ciphertext:", ciphertext)
    
    # Dekripsi
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted = cipher_dec.decrypt(ciphertext)
    print("Decrypted:", decrypted.decode())

Langkah 3 — Implementasi RSA

    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    
    # Generate key pair
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    
    # Enkripsi dengan public key
    cipher_rsa = PKCS1_OAEP.new(public_key)
    plaintext = b"RSA Example"
    ciphertext = cipher_rsa.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    
    # Dekripsi dengan private key
    decipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = decipher_rsa.decrypt(ciphertext)
    print("Decrypted:", decrypted.decode())

---

## 6. Hasil dan Pembahasan

(Hasil eksekusi program Cipher Modern:

!screenshots[Hasil Eksekusi]
)

---

## 7. Jawaban Pertanyaan
1. Perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan:

- DES & AES: menggunakan kunci simetris (satu kunci untuk enkripsi dan dekripsi).

- RSA: menggunakan kunci asimetris (kunci publik dan privat berbeda).

- Keamanan: DES sudah tidak aman (kunci 56-bit mudah dipecahkan), AES sangat aman (hingga 256-bit), RSA juga aman tapi lebih lambat karena berbasis bilangan prima besar.

2. Mengapa AES lebih banyak digunakan dibanding DES di era modern:
Karena AES memiliki ukuran kunci lebih besar (128–256 bit), lebih cepat, dan lebih tahan terhadap serangan brute force dibanding DES.

3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya:
RSA disebut asimetris karena memakai dua kunci berbeda: publik untuk enkripsi dan privat untuk dekripsi.
Kuncinya dibangkitkan dengan memilih dua bilangan prima besar, menghitung hasil kali dan fungsi Eulernya, lalu menghasilkan pasangan kunci publik–privat berdasarkan operasi matematika modular.

---

## 8. Kesimpulan
Cipher modern merupakan dasar utama dalam sistem keamanan data digital.

- DES adalah algoritma simetris generasi awal yang berperan penting dalam sejarah kriptografi, namun kini sudah tidak aman karena ukuran kuncinya kecil (56-bit) dan rentan terhadap serangan brute force.

- AES hadir sebagai penerus DES dengan struktur yang lebih kuat, ukuran kunci yang lebih besar (128–256 bit), dan efisiensi tinggi. Oleh karena itu, AES menjadi standar enkripsi modern yang digunakan secara luas pada jaringan, perangkat mobile, dan sistem keamanan internet.

- RSA berbeda karena bersifat asimetris, menggunakan dua kunci (publik dan privat), dan didasarkan pada kesulitan faktorisasi bilangan prima besar. RSA banyak digunakan untuk pertukaran kunci, tanda tangan digital, dan autentikasi.

Secara keseluruhan, AES unggul dalam kecepatan dan keamanan untuk enkripsi data, sedangkan RSA unggul dalam pengelolaan kunci dan keamanan komunikasi. DES tetap memiliki nilai historis, tetapi tidak lagi digunakan di era modern karena sudah tergantikan oleh algoritma yang lebih kuat dan efisien seperti AES dan RSA

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Rivest, R. L., Shamir, A., & Adleman, L *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*.  
- Stallings, W. *Cryptography and Network Security: Principles and Practice (7th ed.). Pearson Education.*.  )

---

## 10. Commit Log

```
commit abc12345
Author: Subhan Susilo <subhansusilo4@gmail.com>
Date:   2025-11-07

    week6-cipher-modern: implementasi Cipher Modern dan laporan )
```

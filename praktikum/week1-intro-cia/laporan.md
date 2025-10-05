# Laporan Praktikum Kriptografi
Minggu ke-: 01  
Topik: Sejarah Kriptografi & Prinsip CIA  
Nama: Subhan Susilo  
NIM: 230202788 
Kelas: 5IKRA  

## 1. Tujuan
    1. Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
    2. Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
    3. Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
    4. Menyiapkan repositori GitHub sebagai media kerja praktikum.

## 2. Dasar Teori
Sejarah kriptografi adalah ilmu menyandikan informasi dari zaman kuno Yunani dan Romawi hingga era digital modern, sementara Triad CIA (Kerahasiaan, Integritas, Ketersediaan) adalah tiga prinsip fundamental keamanan informasi yang dirumuskan pada tahun 1970-an dan 1980-an untuk melindungi data dari akses tidak sah, modifikasi, dan hilangnya akses yang tidak diinginkan

Kriptografi adalah ilmu dan praktik mengamankan informasi melalui penggunaan algoritma kode, hash, dan tanda tangan untuk melindungi data dari pembacaan yang tidak sah atau manipulasi. Tujuan utamanya adalah mencapai kerahasiaan, integritas, otentikasi, dan non-repudiasi data dengan mengubah informasi yang dapat dibaca (plaintext) menjadi kode yang tidak dapat dipahami (ciphertext) yang hanya dapat didekripsi dengan kunci yang benar. 

Prisip CIA 
1.Confidentiality (Kerahasiaan): Menjamin bahwa informasi hanya dapat diakses oleh pihak yang berwenang. Ini mencegah informasi sensitif jatuh ke tangan yang tidak semestinya.
2.Integrity (Integritas): Memastikan data tetap akurat, lengkap, dan dapat dipercaya, serta tidak dimodifikasi oleh pihak yang tidak berwenang tanpa terdeteksi. 
3.Availability (Ketersediaan): Menjamin bahwa informasi dan sistem dapat diakses oleh pengguna yang berwenang saat dibutuhkan. Ini mencakup melindungi dari bencana alam dan kegagalan sistem. 

A. Caesar Cipher adalah teknik kriptografi klasik berupa sandi substitusi sederhana yang mengganti setiap huruf dalam pesan teks biasa dengan huruf lain di alfabet pada posisi yang tetap, ditentukan oleh sebuah "kunci" angka.

B. Perkembangan kriptografi modern AES diawali pada tahun 2001 ketika National Institute of Standards and Technology (NIST) Amerika Serikat memilih algoritma Rijndael sebagai pengganti Data Encryption Standard (DES) yang sudah usang dan tidak aman lagi.

C. Evolusi kriptografi menuju blockchain kontemporer bermula dari teknik penyandian sederhana menjadi sistem keamanan digital berbasis matematika. Perkembangan seperti kriptografi kunci publik, fungsi hash, dan tanda tangan digital menjadi fondasi utama blockchain. Teknologi ini memungkinkan keamanan, transparansi, dan integritas data tanpa memerlukan otoritas pusat. Dengan kemajuan seperti Zero-Knowledge Proof dan Post-Quantum Cryptography, blockchain terus berkembang menuju sistem yang lebih aman dan efisien di masa depan.

Berikut beberapa contoh peran kriptografi:
    1. Keamanan Data Pribadi
    2. Transaksi Keuangan Digital
    3. Blockchain dan Cryptocurrency
    4. Tanda Tangan Digital dan Sertifikat Elektronik
    5. Perlindungan File dan Sistem Operasi
## 3. Alat dan Bahan

 Python 3.x  

## 4. Langkah Percobaan

1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

## 5. Source Code

# Caesar Cipher - Kriptografi Klasik

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
    
if __name__ == "__main__":
    print("=== Program Caesar Cipher ===")

    encrypted = caesar_encrypt(plaintext, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\n=== Hasil Output ===")
    print("Teks asli     :", plaintext)
    print("Pergeseran    :", shift)
    print("Terenkripsi   :", encrypted)
    print("Didekripsi    :", decrypted)


## 6. Hasil dan Pembahasan
 
( Hasil eksekusi program Caesar Cipher:
![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png) )

## 7. Jawaban Pertanyaan
Soal Quiz:
    1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
    2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
    3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
Jawab:
    1. Tokoh yang dianggap sebagai bapak kriptografi modern adalah Whitfield Diffie bersama Martin Hellman.
Mereka memperkenalkan konsep kriptografi kunci publik (Public Key Cryptography) pada tahun 1976, yang menjadi dasar dari seluruh sistem keamanan digital modern.
    2. Beberapa algoritma kunci publik yang populer digunakan saat ini antara lain: RSA (Rivest–Shamir–Adleman),DSA (Digital Signature Algorithm),ECC (Elliptic Curve Cryptography),dan Diffie–Hellman Key Exchange
    3. Perbedaan antara kriptografi klasik dan kriptografi modern terletak pada dasar keamanan, jenis kunci, media penggunaan, serta tingkat keamanannya.
Kriptografi klasik berfokus pada penyamaran huruf atau pola teks, seperti pada Caesar Cipher dan Vigenère Cipher. Sistem ini umumnya menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi (disebut kunci simetris). Penggunaannya banyak ditemukan pada pesan tertulis atau komunikasi manual, namun kelemahannya adalah mudah dipecahkan dengan komputer modern.
Sebaliknya, kriptografi modern didasarkan pada prinsip matematika yang kompleks, seperti faktorisasi bilangan prima dan logaritma diskret. Sistem ini menggunakan pasangan kunci publik dan privat (asimetris) yang jauh lebih aman. Kriptografi modern diterapkan dalam sistem komputer, jaringan, internet, dan teknologi blockchain, sehingga mampu memberikan tingkat keamanan yang tinggi dan melindungi data dari penyadapan maupun manipulasi.

## 8. Kesimpulan
Kesimpulan Percobaan Teknik Caesar Cipher – Kriptografi Klasik:
Dari percobaan menggunakan teknik Caesar Cipher, dapat disimpulkan bahwa metode ini merupakan bentuk kriptografi klasik yang sangat sederhana. Proses enkripsi dilakukan dengan menggeser huruf dalam teks asli sejumlah nilai tertentu, sedangkan dekripsi dilakukan dengan menggeser huruf ke arah sebaliknya.

Meskipun mudah dipahami dan diterapkan, Caesar Cipher memiliki tingkat keamanan yang rendah, karena pola pergeserannya mudah ditebak dan dapat dipecahkan dengan percobaan sederhana (brute force). Namun demikian, percobaan ini memberikan pemahaman dasar tentang prinsip kerja enkripsi dan dekripsi, yang menjadi fondasi bagi pengembangan kriptografi modern yang lebih kompleks dan aman.


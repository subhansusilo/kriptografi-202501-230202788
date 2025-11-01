# Laporan Praktikum Kriptografi
Minggu ke-: 05  
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
- Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
- Mengimplementasikan algoritma transposisi sederhana.
- Menjelaskan kelemahan algoritma kriptografi klasik.


---

## 2. Dasar Teori
Cipher klasik merupakan metode kriptografi sederhana yang digunakan pada masa awal perkembangan ilmu keamanan informasi untuk menyembunyikan pesan rahasia. Tiga jenis cipher klasik yang paling dikenal adalah Caesar Cipher, Vigenère Cipher, dan Transposisi Cipher.

Caesar Cipher merupakan bentuk paling dasar dari substitution cipher, di mana setiap huruf dalam teks asli digeser dengan jumlah tertentu dalam alfabet. Misalnya, jika menggunakan kunci pergeseran 3, maka huruf A menjadi D, B menjadi E, dan seterusnya. Contohnya, kata “HELLO” dengan kunci 3 akan dienkripsi menjadi “KHOOR”. Cipher ini sangat mudah digunakan, tetapi juga mudah dipecahkan dengan metode brute force karena hanya memiliki 25 kemungkinan kunci.

Vigenère Cipher adalah pengembangan dari Caesar Cipher yang menggunakan kata kunci sebagai dasar pergeseran huruf. Setiap huruf dalam kunci menentukan besar pergeseran yang berbeda pada setiap huruf teks asli. Misalnya, teks “ATTACKATDAWN” dengan kunci “LEMON” akan menghasilkan ciphertext “LXFOPVEFRNHR”. Karena pergeseran berubah-ubah berdasarkan kunci, cipher ini jauh lebih sulit dipecahkan dibanding Caesar Cipher dan termasuk dalam kategori polyalphabetic cipher.

Berbeda dengan dua cipher sebelumnya, Transposisi Cipher tidak mengganti huruf dalam teks, tetapi mengubah urutannya. Metode ini mengacak posisi huruf sesuai pola tertentu, misalnya berdasarkan kolom atau baris dari kunci yang diberikan. Contohnya, dalam columnar transposition, teks “MEETMEAFTERTHEPARTY” dengan kunci urutan kolom tertentu dapat menghasilkan ciphertext yang terlihat acak.

Secara umum, Caesar Cipher, Vigenère Cipher, dan Transposisi Cipher menunjukkan bagaimana teknik enkripsi klasik bekerja melalui substitusi dan permutasi huruf. Meskipun keamanan ketiganya tergolong rendah bila dibandingkan dengan sistem enkripsi modern seperti AES atau RSA, cipher klasik tetap memiliki nilai historis dan edukatif dalam memahami dasar-dasar kriptografi

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat file `Cipher Klasik.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python Cipher Klasik.py`.)

---

## 5. Source Code
Langkah 1 — Implementasi Caesar Cipher

        def caesar_encrypt(plaintext, key):
            result = ""
            for char in plaintext:
                if char.isalpha():
                    shift = 65 if char.isupper() else 97
                    result += chr((ord(char) - shift + key) % 26 + shift)
                else:
                    result += char
            return result

        def caesar_decrypt(ciphertext, key):
            return caesar_encrypt(ciphertext, -key)

        # Contoh uji
        msg = "CLASSIC CIPHER"
        key = 3
        enc = caesar_encrypt(msg, key)
        dec = caesar_decrypt(enc, key)
        print("Plaintext :", msg)
        print("Ciphertext:", enc)
        print("Decrypted :", dec)

Langkah 2 — Implementasi Vigenère Cipher

        def vigenere_encrypt(plaintext, key):
            result = []
            key = key.lower()
            key_index = 0
            for char in plaintext:
                if char.isalpha():
                    shift = ord(key[key_index % len(key)]) - 97
                    base = 65 if char.isupper() else 97
                    result.append(chr((ord(char) - base + shift) % 26 + base))
                    key_index += 1
                else:
                    result.append(char)
            return "".join(result)
        
        def vigenere_decrypt(ciphertext, key):
            result = []
            key = key.lower()
            key_index = 0
            for char in ciphertext:
                if char.isalpha():
                    shift = ord(key[key_index % len(key)]) - 97
                    base = 65 if char.isupper() else 97
                    result.append(chr((ord(char) - base - shift) % 26 + base))
                    key_index += 1
                else:
                    result.append(char)
            return "".join(result)
        
        # Contoh uji
        msg = "KRIPTOGRAFI"
        key = "KEY"
        enc = vigenere_encrypt(msg, key)
        dec = vigenere_decrypt(enc, key)
        print("Plaintext :", msg)
        print("Ciphertext:", enc)
        print("Decrypted :", dec)

Langkah 3 — Implementasi Transposisi Sederhana

        def transpose_encrypt(plaintext, key=5):
            ciphertext = [''] * key
            for col in range(key):
                pointer = col
                while pointer < len(plaintext):
                    ciphertext[col] += plaintext[pointer]
                    pointer += key
            return ''.join(ciphertext)
        
        def transpose_decrypt(ciphertext, key=5):
            num_of_cols = int(len(ciphertext) / key + 0.9999)
            num_of_rows = key
            num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
            plaintext = [''] * num_of_cols
            col = 0
            row = 0
            for symbol in ciphertext:
                plaintext[col] += symbol
                col += 1
                if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
                    col = 0
                    row += 1
            return ''.join(plaintext)
        
        # Contoh uji
        msg = "TRANSPOSITIONCIPHER"
        enc = transpose_encrypt(msg, key=5)
        dec = transpose_decrypt(enc, key=5)
        print("Plaintext :", msg)
        print("Ciphertext:", enc)
        print("Decrypted :", dec)

---

## 6. Hasil dan Pembahasan
 Hasil eksekusi program Cipher Klasik:

![Hasil Screenshots caesar]
![Hasil Screenshots vigenere]
![Hasil Screenshots transpose]


---

## 7. Jawaban Pertanyaan
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?

Jawab: Kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher terletak pada sifat substitusi huruf yang masih terlalu sederhana. Caesar Cipher hanya menggunakan satu kunci berupa pergeseran tetap untuk seluruh huruf dalam pesan, sehingga memiliki ruang kunci yang sangat kecil (hanya 25 kemungkinan). Akibatnya, cipher ini mudah dipecahkan dengan metode brute force atau frequency analysis. Sementara itu, Vigenère Cipher memang lebih kuat karena menggunakan kunci berupa kata yang mengubah pergeseran tiap huruf, namun jika kuncinya pendek atau berulang, pola frekuensi huruf tetap bisa muncul. Dengan teknik seperti Kasiski examination atau index of coincidence, penyerang dapat menemukan panjang kunci dan kemudian memecahkannya menjadi beberapa Caesar Cipher yang lebih kecil.

2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?

Jawab:Cipher klasik mudah diserang dengan analisis frekuensi karena huruf-huruf dalam bahasa alami (seperti Bahasa Indonesia atau Inggris) tidak muncul dengan frekuensi yang sama. Misalnya, dalam bahasa Inggris huruf E, T, dan A paling sering muncul. Dalam cipher substitusi seperti Caesar atau Vigenère (dengan kunci pendek), pola kemunculan huruf-huruf tersebut tetap terlihat, hanya bergeser atau terganti. Dengan membandingkan frekuensi huruf dalam ciphertext dengan distribusi huruf umum suatu bahasa, penyerang dapat menebak huruf-huruf aslinya dan memulihkan pesan.

3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi
Jawab:Jika dibandingkan antara cipher substitusi dan cipher transposisi, masing-masing memiliki kelebihan dan kelemahan. Cipher substitusi (seperti Caesar dan Vigenère) mengganti huruf dengan huruf lain, sehingga pola posisi huruf hilang, tetapi frekuensi huruf tetap bisa terdeteksi. Sebaliknya, cipher transposisi tidak mengubah huruf, hanya mengacak urutannya, sehingga distribusi frekuensi huruf tetap sama seperti teks asli. Akibatnya, cipher substitusi lebih rentan terhadap analisis frekuensi, sedangkan cipher transposisi lebih rentan terhadap serangan yang mencoba menebak pola pengacakan. Dalam praktiknya, keamanan dapat ditingkatkan dengan menggabungkan keduanya, yaitu melakukan substitusi terlebih dahulu lalu transposisi, agar pesan lebih sulit diuraikan

---

## 8. Kesimpulan
Cipher klasik seperti Caesar Cipher, Vigenère Cipher, dan Transposisi Cipher merupakan dasar dari ilmu kriptografi yang menunjukkan dua prinsip utama enkripsi, yaitu substitusi (penggantian huruf) dan transposisi (pengacakan posisi huruf). Caesar Cipher menggunakan pergeseran huruf tetap, sedangkan Vigenère Cipher menggunakan kunci berupa kata untuk menghasilkan pergeseran yang bervariasi, dan Transposisi Cipher mengubah urutan huruf tanpa menggantinya.

Namun, baik Caesar maupun Vigenère Cipher memiliki kelemahan karena pola frekuensi huruf dalam bahasa masih dapat terdeteksi, sehingga mudah diserang menggunakan analisis frekuensi. Caesar Cipher sangat lemah karena hanya memiliki sedikit kemungkinan kunci, sementara Vigenère Cipher bisa dipecahkan dengan metode seperti Kasiski examination jika kuncinya pendek atau berulang.

Secara umum, cipher substitusi lebih rentan terhadap serangan berbasis pola huruf, sedangkan cipher transposisi lebih lemah terhadap serangan yang menebak struktur atau urutan teks. Oleh karena itu, cipher klasik dianggap tidak aman untuk digunakan dalam komunikasi modern, namun tetap penting sebagai dasar pemahaman prinsip enkripsi yang menjadi fondasi bagi sistem kriptografi modern seperti AES dan RSA.

---

## 9. Daftar Pustaka  
- Christensen, S. *Cryptanalysis of the Vigenère Cipher*.  
- Devi, Harshini.*Analysis and Comparison of Substitution and Transposition Methods in Cryptographic Systems.*.  

---

## 10. Commit Log
```
commit abc12345
Author: Subhan Susilo <subhansusilo@gmail.com>
Date:   2025-11-01

    week5-cipher-klasik: implementasi Caesar Klasik dan laporan )
```

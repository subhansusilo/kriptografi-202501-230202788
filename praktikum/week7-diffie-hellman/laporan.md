# Laporan Praktikum Kriptografi
Minggu ke-: 07  
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
- Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
- Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Diffie–Hellman adalah protokol pertukaran kunci yang memungkinkan dua pihak menciptakan shared secret secara aman meskipun komunikasi dilakukan lewat saluran publik. Intinya, masing-masing pihak memilih kunci privat, lalu menghasilkan kunci publik menggunakan operasi pangkat modulo bilangan prima besar. Setelah saling bertukar kunci publik, kedua pihak melakukan perhitungan ulang sehingga menghasilkan nilai rahasia yang identik, walaupun tidak pernah mengirimkan nilai rahasia itu secara langsung.

Mekanisme Diffie–Hellman
- Dua nilai publik disepakati: bilangan prima p dan generator g.
- Masing-masing memilih kunci privat: Alice memilih a, Bob memilih b (dirahasiakan).
- Menghitung kunci publik:
    - Alice: A = gᵃ mod p

    - Bob: B = gᵇ mod p
- Tukar kunci publik: A dan B dikirim lewat saluran publik.
- Hitung shared secret:
    - Alice: S = Bᵃ mod p
    - Bob: S = Aᵇ mod p
      
        Hasilnya sama: S = g^(ab) mod p.
- Shared secret ini lalu dipakai sebagai dasar kunci enkripsi simetris.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
  

---

## 4. Langkah Percobaan
1. Membuat file `diffie_hellman.py` di folder `praktikum/week7-diffie-hellman/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python diffie_hellman.py`.)

---

## 5. Source Code
    import random
    
    parameter umum (disepakati publik)
    
    p = 23  # bilangan prima
    
    g = 5   # generator

    
    private key masing-masing pihak
    
    a = random.randint(1, p-1)  # secret Alice
    
    b = random.randint(1, p-1)  # secret Bob

    
    public key
    
    A = pow(g, a, p)
    
    B = pow(g, b, p)

    
    exchange public key
    
    shared_secret_A = pow(B, a, p)
    
    shared_secret_B = pow(A, b, p)

    
    print("Kunci bersama Alice :", shared_secret_A)
    
    print("Kunci bersama Bob   :", shared_secret_B)

---

## 6. Hasil dan Pembahasan 

Hasil eksekusi program diffie-hellman:


---

## 7. Jawaban Pertanyaan

1. Mengapa Diffie–Hellman memungkinkan pertukaran kunci di saluran publik?

    Karena kedua pihak tidak pernah mengirimkan kunci rahasia secara langsung.
    Mereka hanya bertukar kunci publik yang aman dilihat siapa saja. Dengan rumus matematika (pangkat modulo), masing-masing bisa menghitung shared secret yang sama tanpa membocorkan kunci privat. Penyerang yang melihat data publik tetap tidak bisa menebak kunci rahasianya karena harus memecahkan discrete logarithm, yang sangat sulit secara komputasi.

2. Apa kelemahan utama protokol Diffie–Hellman murni?

    Kelemahan utamanya: tidak ada autentikasi.
    Artinya, protokol ini tidak bisa memastikan apakah kunci publik yang diterima benar-benar milik pihak yang dituju. Tanpa identitas yang terverifikasi, penyerang dapat menyamar sebagai salah satu pihak dan menyusup ke dalam proses pertukaran kunci.

3. Bagaimana cara mencegah serangan MITM pada protokol ini?

    Serangan MITM bisa dicegah dengan menambahkan autentikasi. Dalam praktik modern, biasanya digunakan:
    - Digital signature (penandatanganan kunci publik).
    - Sertifikat digital (CA) seperti pada HTTPS/TLS.
    - Password Authenticated Key Exchange (PAKE) untuk sistem yang memakai kata sandi.
    Prinsipnya: pastikan identitas pihak yang bertukar kunci dapat diverifikasi sehingga penyerang tidak bisa menyisipkan kunci palsu.

---

## 8. Kesimpulan
Diffie–Hellman merupakan mekanisme pertukaran kunci yang memungkinkan dua pihak membangun kunci rahasia bersama meskipun berkomunikasi melalui saluran yang tidak aman. Keunggulan utamanya terletak pada penggunaan operasi matematika pangkat modulo, sehingga kunci publik yang dikirim tidak dapat digunakan untuk menebak kunci privat. Hal ini membuat proses pembentukan kunci tetap aman meskipun penyerang dapat melihat data yang dipertukarkan.

Namun, protokol Diffie–Hellman murni memiliki kekurangan mendasar karena tidak menyertakan autentikasi. Tanpa verifikasi identitas, pihak yang terlibat tidak dapat memastikan apakah kunci publik yang diterima benar-benar dari sumber yang sah. Celah inilah yang membuka peluang bagi serangan Man-in-the-Middle, di mana penyerang dapat menyisipkan diri di antara kedua pihak dan membentuk dua kunci berbeda untuk kemudian memata-matai komunikasi.

Untuk mencegah MITM, protokol ini perlu dikombinasikan dengan mekanisme autentikasi tambahan seperti digital signature, sertifikat digital, atau metode verifikasi lainnya. Pendekatan ini memastikan bahwa setiap kunci publik yang diterima sudah terjamin keasliannya, sehingga proses pembentukan kunci bersama berjalan aman. Dengan demikian, Diffie–Hellman menjadi jauh lebih kuat ketika dipadukan dengan sistem autentikasi modern yang sudah umum digunakan pada protokol seperti TLS/HTTPS

---

## 9. Daftar Pustaka

- Diffie, W., & Hellman, M. *New Directions in Cryptography. IEEE Transactions on Information Theory*.  
- Kadir, A. *Pengenalan Kriptografi: Teori dan Implementasi*.  

---

## 10. Commit Log

```
commit abc12345
Author: Subhan Susilo <subhansusilo01@gmail.com>
Date:   2025-11-25

    week7-diffie-hellman: implementasi diffie-hellman dan laporan )
```

# Laporan Praktikum Kriptografi
Minggu ke-   : 03  
Topik        : [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama         : [Subhan Susilo]     
NIM          : [230202788]  
Kelas        : [5IKRA]  

---

## 1. Tujuan

1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.


---

## 2. Dasar Teori
Aritmetika Modular atau Modular Math merupakan sistem operasi bilangan yang bekerja berdasarkan sisa hasil pembagian suatu bilangan terhadap bilangan tertentu yang disebut modulus. Dalam sistem ini, dua bilangan dikatakan kongruen jika keduanya memiliki sisa yang sama ketika dibagi oleh modulus, misalnya 
17≡5(mod12). Konsep ini banyak digunakan dalam kehidupan sehari-hari, seperti sistem waktu (jam), dan menjadi dasar penting dalam kriptografi karena operasi enkripsi dan dekripsi sering dilakukan dalam bentuk modular.

Selanjutnya, GCD (Greatest Common Divisor) atau Faktor Persekutuan Terbesar (FPB) adalah bilangan terbesar yang dapat membagi dua bilangan tanpa menyisakan sisa. Konsep ini penting untuk menentukan apakah dua bilangan bersifat coprime (saling prima), yaitu tidak memiliki faktor persekutuan selain 1. Dalam kriptografi, terutama pada algoritma RSA, GCD digunakan untuk memastikan kunci publik dan privat dapat berfungsi dengan benar, sebab syarat utamanya adalah kedua bilangan harus saling prima.

Kemudian, bilangan prima adalah bilangan yang hanya memiliki dua faktor, yaitu 1 dan dirinya sendiri. Contohnya 2, 3, 5, 7, dan 11. Bilangan prima memiliki peran yang sangat penting dalam sistem keamanan kriptografi modern karena sifatnya yang sulit difaktorkan. Sistem seperti RSA menggunakan dua bilangan prima besar untuk membentuk modulus, dan keamanan algoritma tersebut didasarkan pada sulitnya memfaktorkan hasil perkalian dari dua bilangan prima besar tersebut.

Terakhir, logaritma diskrit (discrete logarithm) adalah versi modular dari logaritma biasa. Jika 
ax≡b(modN) maka nilai x disebut logaritma diskrit dari b dengan basis a pada modulus n. Meskipun mudah menghitung 
ax(modn), sebaliknya—menentukan x dari a dan b—sangat sulit, terutama untuk modulus yang besar. Kesulitan inilah yang dimanfaatkan dalam berbagai algoritma kriptografi modern seperti Diffie–Hellman dan ElGamal.

Secara keseluruhan, keempat konsep ini saling berhubungan dan membentuk dasar kuat bagi teori bilangan dalam kriptografi. Aritmetika modular menjadi sistem operasinya, GCD memastikan bilangan yang digunakan saling bebas faktor, bilangan prima menjadi bahan pembentuk keamanan, dan logaritma diskrit menjadi masalah matematis yang sulit dipecahkan sehingga menjamin kerahasiaan data dalam sistem keamanan digital.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan

1. Membuat file `modular_math.py` di folder `praktikum/week3-modmath-gcd/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python modular_math.py`.

---

## 5. Source Code
1. Aritmetika Modular

        def mod_add(a, b, n): return (a + b) % n
        def mod_sub(a, b, n): return (a - b) % n
        def mod_mul(a, b, n): return (a * b) % n
        def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

        print("7 + 5 mod 12 =", mod_add(7, 5, 12))
        print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
        print("7^128 mod 13 =", mod_exp(7, 128, 13))

2. GCD & Algoritma Euclidean

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        print("gcd(54, 24) =", gcd(54, 24))
   
3. Extended Euclidean Algorithm

        def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        return g, y1 - (b // a) * x1, x1

        def modinv(a, n):
            g, x, _ = egcd(a, n)
            if g != 1:
                return None
            return x % n

        print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

4. Logaritma Diskrit (Discrete Log)

        def discrete_log(a, b, n):
            for x in range(n):
                if pow(a, x, n) == b:
                    return x
            return None

        print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4

---

## 6. Hasil dan Pembahasan
Dari keempat code yang telah dibuat — yaitu operasi aritmetika modular, GCD (Greatest Common Divisor), invers modular, dan logaritma diskrit — dapat disimpulkan bahwa semuanya saling berkaitan dalam membentuk dasar sistem kriptografi modern. Kode pertama menunjukkan bagaimana operasi dasar seperti penjumlahan, perkalian, dan perpangkatan dapat dilakukan secara efisien dalam ruang modular, yang menjadi pondasi dari enkripsi dan dekripsi pada algoritma seperti RSA.

Kode kedua dan ketiga, yaitu fungsi GCD dan invers modular, berperan penting dalam memastikan hubungan antara dua bilangan. Fungsi GCD digunakan untuk menentukan apakah dua bilangan saling prima, sedangkan invers modular memungkinkan pembalikan proses enkripsi menjadi dekripsi dalam sistem kunci publik. Tanpa invers modular, proses pengembalian pesan asli dari ciphertext tidak dapat dilakukan.

Terakhir, kode keempat tentang logaritma diskrit menggambarkan betapa sulitnya menemukan nilai eksponen x dari persamaan ax≡b(modn) — inilah yang menjadi dasar keamanan algoritma seperti Diffie–Hellman. Secara keseluruhan, keempat kode ini memperlihatkan hubungan erat antara konsep matematika dasar dan penerapannya dalam menjaga keamanan data digital melalui kriptografi. 

Hasil eksekusi program modular_math:

![Hasil Eksekusi](screenshots/output.png)

---

## 7. Jawaban Pertanyaan
1. Apa peran aritmetika modular dalam kriptografi modern?
Jawab: Aritmetika modular berperan sebagai dasar utama dalam semua operasi matematis kriptografi modern. Sistem ini memungkinkan proses enkripsi dan dekripsi dilakukan dalam ruang bilangan terbatas menggunakan operasi seperti penjumlahan, perkalian, dan perpangkatan dengan mengambil sisa pembagian terhadap suatu modulus. Dengan kata lain, aritmetika modular menjaga agar hasil operasi tetap berada dalam rentang bilangan yang dapat diprediksi namun tetap sulit ditebak tanpa kunci yang benar. Dalam algoritma seperti RSA, Diffie–Hellman, dan ElGamal, perhitungan kunci, enkripsi, dan dekripsi semuanya bergantung pada operasi modular, sehingga keamanan sistem kriptografi bergantung pada sifat-sifat unik dari aritmetika modular ini.

2. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
Jawab: Invers modular sangat penting karena digunakan untuk mencari kunci dekripsi yang sesuai dengan kunci enkripsi. Dalam algoritma RSA, proses pembuatan kunci melibatkan dua bilangan e (kunci publik) dan d (kunci privat) yang saling berhubungan melalui persamaan:(e×d)≡1(modφ(n))
Di sini, d adalah invers modular dari e terhadap φ(n) (fungsi totien Euler). Artinya, ketika pesan terenkripsi dipangkatkan dengan d (mod N), hasilnya akan mengembalikan pesan asli. Tanpa invers modular, proses dekripsi tidak dapat dilakukan, karena tidak ada cara matematis untuk membalikkan hasil enkripsi dengan aman. Oleh sebab itu, invers modular menjadi komponen krusial dalam memastikan bahwa hanya pemilik kunci privat yang bisa membuka pesan terenkripsi.

3. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
Jawab: Tantangan utamanya terletak pada kompleksitas komputasi yang sangat tinggi. Untuk modulus besar (misalnya ratusan atau ribuan bit), tidak ada algoritma efisien yang mampu menghitung logaritma diskrit dalam waktu yang wajar. Proses mencari nilai x dari persamaan 
ax≡b(modn)menjadi sangat sulit karena jumlah kemungkinan nilai x yang harus dicoba sangat besar, dan tidak ada pola sederhana yang bisa dimanfaatkan. Kesulitan inilah yang menjadi dasar keamanan dari algoritma seperti Diffie–Hellman Key Exchange dan ElGamal, karena meskipun mudah menghitung hasil perpangkatan modular, membalikkan prosesnya (menemukan eksponen x) hampir mustahil dilakukan secara praktis tanpa kunci yang benar.

---

## 8. Kesimpulan
Konsep Modular Math yang meliputi Aritmetika Modular, GCD, Bilangan Prima, dan Logaritma Diskrit merupakan fondasi utama dalam teori bilangan yang menjadi dasar kriptografi modern. Aritmetika modular digunakan untuk melakukan operasi matematika seperti penjumlahan, perkalian, dan perpangkatan dengan mengambil sisa hasil pembagian terhadap suatu modulus. Dengan cara ini, setiap hasil operasi tetap berada dalam ruang bilangan terbatas namun tetap aman dan efisien untuk digunakan dalam algoritma kriptografi seperti RSA dan Diffie–Hellman.

Selanjutnya, GCD (Greatest Common Divisor) berperan penting dalam menentukan apakah dua bilangan saling prima (coprime), yang menjadi syarat utama agar proses pembentukan kunci publik dan kunci privat dapat dilakukan dengan benar. Bilangan yang saling prima akan memiliki invers modular, yaitu bilangan yang digunakan untuk membalik proses enkripsi menjadi dekripsi. Selain itu, bilangan prima menjadi dasar dalam pembentukan sistem keamanan kriptografi karena modulus pada algoritma seperti RSA dibangun dari hasil kali dua bilangan prima besar. Keamanan algoritma tersebut bergantung pada sulitnya memfaktorkan hasil kali bilangan prima tersebut.

Kemudian, logaritma diskrit menjadi komponen matematis yang menjamin tingkat keamanan tinggi pada sistem berbasis kunci publik seperti Diffie–Hellman dan ElGamal. Kesulitan utama dalam menyelesaikan logaritma diskrit untuk modulus besar membuat proses menemukan eksponen x dari persamaan 
ax≡b(modn)hampir mustahil dilakukan tanpa kunci yang tepat. Melalui penerapan keempat konsep ini—mulai dari operasi modular, pencarian GCD, peran bilangan prima, hingga kesulitan logaritma diskrit—sistem kriptografi modern dapat menjaga kerahasiaan, integritas, dan keamanan data digital secara efektif

---

## 9. Daftar Pustaka
  
- Kak, A. *Prime Numbers And Discrete Logarithms*.  
- GeeksforGeeks. *Modular Arithmetic*.  

---

## 10. Commit Log

commit week03  
Author: Subhan Susilo <subhansusilo4@gmail.com>  
Date:   2025-10-20

    week3-Modular Math-Gcd: implementasi modular arithmetic & GCD dan laporan )
```

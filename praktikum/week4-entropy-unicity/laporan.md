# Laporan Praktikum Kriptografi
Minggu ke-: 04  
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.


---

## 2. Dasar Teori
  Entropy dan Unicity Distance merupakan dua konsep penting dalam evaluasi kekuatan kunci kriptografi terhadap serangan brute force. Entropy menggambarkan tingkat keacakan atau ketidakpastian suatu kunci. Semakin tinggi nilai entropi, semakin sulit kunci tersebut ditebak karena setiap kemungkinan memiliki peluang yang sama untuk dipilih. Nilai entropi biasanya dinyatakan dalam bit, dan jika sebuah kunci memiliki entropi sebesar n bit, maka dibutuhkan sekitar 2n percobaan untuk menemukan kunci yang benar melalui brute force. Oleh karena itu, kunci yang benar-benar acak dan panjang akan memiliki entropi tinggi serta tingkat keamanan yang lebih baik dibandingkan kunci yang mudah ditebak atau memiliki pola tertentu.

  Sementara itu, Unicity Distance adalah jumlah minimum ciphertext yang dibutuhkan agar hanya terdapat satu kunci yang cocok dengan plaintext yang bermakna. Konsep ini diperkenalkan oleh Claude Shannon untuk menilai seberapa banyak informasi yang diperlukan agar suatu cipher dapat dipecahkan secara pasti. Nilai unicity distance dihitung dari rasio antara entropi kunci dan redundansi plaintext. Jika ciphertext yang tersedia lebih sedikit dari nilai ini, masih banyak kemungkinan kunci yang dapat menghasilkan plaintext masuk akal, namun jika jumlah ciphertext melebihi unicity distance, maka kunci yang benar dapat ditemukan secara unik. 

  Hubungan antara entropi dan unicity distance menunjukkan bahwa semakin tinggi entropi suatu kunci, semakin besar pula nilai unicity distance-nya, sehingga cipher menjadi lebih sulit dipecahkan. Meskipun algoritma modern seperti AES dan RSA memiliki keamanan matematis yang sangat kuat, serangan brute force tetap menjadi ancaman apabila kunci yang digunakan tidak cukup acak atau terlalu pendek. Brute force bekerja dengan mencoba semua kemungkinan kunci, dan dengan kemajuan teknologi seperti GPU dan komputasi paralel, proses ini dapat dilakukan lebih cepat. Dengan demikian, evaluasi kekuatan kunci melalui nilai entropi dan unicity distance menjadi sangat penting untuk memastikan bahwa sistem kriptografi benar-benar tahan terhadap serangan brute force dan menjaga kerahasiaan data secara optimal.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat file `entropy_unicity.py` di folder `praktikum/week4-entropy-unicity/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python entropy_unicity.py`.

---

## 5. Source Code
Langkah 1 — Perhitungan Entropi

    import math

    def entropy(keyspace_size):
        return math.log2(keyspace_size)

    print("Entropy ruang kunci 26 =", entropy(26), "bit")
    print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

Langkah 2 — Menghitung Unicity Distance

    def unicity_distance(HK, R=0.75, A=26):
        return HK / (R * math.log2(A))

    HK = entropy(26)
    print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

Langkah 3 — Analisis Brute Force

    def brute_force_time(keyspace_size, attempts_per_second=1e6):
        seconds = keyspace_size / attempts_per_second
        days = seconds / (3600*24)
        return days

    print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
    print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program entropy_unicity:

![Hasil Eksekusi](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?
- Entropy menunjukkan seberapa acak dan tidak terduga sebuah kunci.
- Nilai entropy yang tinggi berarti setiap kemungkinan kunci memiliki peluang yang sama untuk digunakan, sehingga penyerang tidak bisa menebak pola atau mengurangi ruang pencarian.
- Misalnya:
    - Kunci 128-bit acak → entropi = 128 bit → ada 2pangkat(128)kemungkinan kunci.
    - Kunci berbasis kata sandi sederhana → entropinya jauh lebih rendah → mudah ditebak.

- Kesimpulan: Semakin tinggi entropi, semakin kuat kunci terhadap serangan tebakan dan brute force.

2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
- Unicity distance menunjukkan berapa banyak ciphertext yang diperlukan agar penyerang bisa menentukan satu kunci yang benar-benar unik.
- Jika ciphertext yang tersedia kurang dari nilai unicity distance, masih banyak kemungkinan kunci yang bisa menghasilkan plaintext “masuk akal”, jadi kunci belum bisa dipastikan.
- Jika ciphertext lebih dari unicity distance, maka cipher menjadi tertentu (deterministic) dan dapat dipecahkan secara teoritis.
- Kesimpulan: Semakin besar unicity distance → semakin sulit bagi penyerang menemukan kunci unik → cipher lebih aman.

3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
- Karena brute force tidak menyerang kelemahan algoritma, tapi memeriksa semua kemungkinan kunci.
- Jika pengguna memakai kunci lemah, pendek, atau tidak acak, brute force masih bisa berhasil walau algoritmanya aman.
- Selain itu, kemajuan teknologi komputasi (GPU, cloud, dan komputasi kuantum) membuat brute force semakin cepat.
- Kesimpulan: Algoritma kuat belum cukup — kunci harus panjang, acak, dan dijaga baik agar brute force tetap tidak praktis.

---

## 8. Kesimpulan
Dari hasil perhitungan dan analisis, dapat disimpulkan bahwa entropi dan unicity distance merupakan indikator utama dalam menilai kekuatan kunci kriptografi. Entropi menggambarkan tingkat keacakan suatu kunci — semakin tinggi entropinya, semakin besar pula ruang kunci yang harus dijelajahi oleh penyerang, sehingga serangan brute force menjadi tidak praktis. Sementara itu, unicity distance menunjukkan seberapa banyak ciphertext yang dibutuhkan agar kunci dapat ditemukan secara unik. Cipher dengan nilai unicity distance yang kecil, seperti Caesar Cipher, sangat mudah dipecahkan karena hanya memerlukan sedikit data untuk menemukan kunci yang benar. Sebaliknya, algoritma modern seperti AES memiliki entropi tinggi dan unicity distance besar, menjadikannya sangat tahan terhadap analisis dan serangan brute force. Dengan demikian, semakin besar entropi dan unicity distance suatu sistem kriptografi, semakin kuat pula keamanannya terhadap serangan berbasis pencarian kunci, meskipun perkembangan teknologi komputasi tetap menuntut perlunya pemilihan kunci yang panjang, acak, dan aman dalam implementasi nyata

---

## 9. Daftar Pustaka
- Yue Wu, Joseph P. Noonan, Sos Agaian. *Shannon Entropy based Randomness Measurement and Test for Image Encryption*.  
- Chong Xiang & Li Yang. *Unicity Distance of Quantum Encryption Protocols*.
- Fangyuan Lin. *Revisiting the Unicity Distance through a Channel Transmission Perspective* 

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week4-entropy-unicity: implementasi Caesar Cipher dan laporan )
```

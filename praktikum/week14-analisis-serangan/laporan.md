# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Analisis Serangan Kriptografi]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Mengidentifikasi jenis serangan pada sistem informasi nyata.
- Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
- Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori

Analisis serangan kriptografi adalah proses sistematis untuk mengidentifikasi, memahami, dan mengevaluasi berbagai cara yang dapat digunakan penyerang untuk melemahkan atau menembus sistem kriptografi. Tujuan utamanya bukan sekadar “membobol” algoritma, tetapi menilai seberapa kuat mekanisme keamanan dalam menjaga kerahasiaan, integritas, dan keaslian data ketika dihadapkan pada asumsi realistis tentang kemampuan penyerang. Dalam analisis ini, biasanya dipertimbangkan berbagai model serangan, seperti ciphertext-only attack, known-plaintext attack, chosen-plaintext attack, hingga chosen-ciphertext attack, yang masing-masing menguji ketahanan sistem pada tingkat akses informasi yang berbeda.

Namun, asumsi yang sering keliru adalah menganggap serangan kriptografi selalu berarti kelemahan matematis pada algoritma inti. Pada praktiknya, banyak serangan justru mengeksploitasi kesalahan implementasi, manajemen kunci yang buruk, atau faktor non-teknis seperti side-channel attacks (misalnya analisis waktu eksekusi atau konsumsi daya). Ini menunjukkan bahwa kekuatan kriptografi tidak hanya ditentukan oleh desain algoritma, tetapi juga oleh konteks penggunaannya. Dari sudut pandang skeptis, sistem yang secara teoritis aman tetap dapat gagal jika tidak dianalisis secara menyeluruh terhadap skenario serangan nyata.

Dengan demikian, analisis serangan kriptografi berfungsi sebagai alat evaluasi kritis untuk menguji asumsi keamanan yang sering dianggap “aman secara default”. Pendekatan ini mendorong perancang sistem untuk berpikir seperti penyerang, menguji batas logika keamanan, dan mengadopsi perspektif alternatif bahwa keamanan adalah sifat sistem secara keseluruhan, bukan sekadar algoritma. Hasil analisis ini menjadi dasar penting dalam meningkatkan desain, implementasi, dan kebijakan penggunaan kriptografi agar lebih tahan terhadap ancaman yang terus berkembang.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  )

---

## 4. Langkah Percobaan


---

## 5. Source Code


---

## 6. Hasil dan Pembahasan


---

## 7. Jawaban Pertanyaan

1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Banyak sistem lama dirancang pada masa ketika kapasitas komputasi masih terbatas, sehingga panjang kunci, kompleksitas algoritma, dan mekanisme perlindungan kata sandi dianggap sudah memadai untuk zamannya. Asumsi ini kini tidak lagi valid: peningkatan daya komputasi, GPU, dan komputasi terdistribusi membuat serangan brute force dan dictionary jauh lebih murah dan cepat. Selain itu, sistem lama sering menggunakan fungsi hash yang lemah atau tidak dirancang khusus untuk penyimpanan kata sandi (misalnya tanpa salt dan key stretching), serta jarang diperbarui karena alasan kompatibilitas atau biaya. Bias kognitif yang sering muncul di sini adalah status quo bias: sistem dianggap “aman” hanya karena telah lama digunakan tanpa insiden besar.

2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Kelemahan algoritma bersumber dari desain matematis atau logika kriptografinya, misalnya struktur yang memungkinkan penyerang mengurangi kompleksitas pencarian kunci atau menemukan pola tertentu. Jika algoritmanya lemah, maka sebaik apa pun implementasinya, sistem tetap tidak aman. Sebaliknya, kelemahan implementasi terjadi ketika algoritma yang secara teoritis kuat diterapkan dengan cara yang salah, seperti manajemen kunci yang buruk, penggunaan parameter default yang tidak aman, atau kebocoran informasi melalui side-channel. Perbedaan pentingnya: kelemahan algoritma bersifat fundamental dan universal, sedangkan kelemahan implementasi bersifat kontekstual dan sering kali bisa diperbaiki tanpa mengganti algoritma itu sendiri.

3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Tidak ada jaminan keamanan yang bersifat permanen, sehingga fokusnya harus pada adaptability, bukan kepastian mutlak. Organisasi perlu menerapkan algoritma dan protokol yang telah distandarkan dan ditinjau secara luas, disertai kebijakan pembaruan berkala mengikuti perkembangan riset kriptografi. Audit keamanan, penetration testing, dan threat modeling perlu dilakukan secara rutin untuk menguji asumsi keamanan yang ada. Selain itu, desain sistem sebaiknya bersifat crypto-agile, yaitu memungkinkan penggantian algoritma atau parameter tanpa harus merombak seluruh infrastruktur. Perspektif ini menantang asumsi bahwa “sekali aman, selamanya aman” dan menempatkan keamanan kriptografi sebagai proses berkelanjutan, bukan kondisi statis.

---

## 8. Kesimpulan

Secara keseluruhan, kerentanan pada sistem kriptografi sering kali bukan semata akibat algoritma yang lemah, melainkan karena asumsi lama yang tidak lagi relevan, implementasi yang keliru, dan kegagalan beradaptasi dengan perkembangan ancaman. Serangan seperti brute force dan dictionary attack menunjukkan bahwa keamanan bersifat dinamis dan sangat dipengaruhi oleh kemajuan teknologi serta praktik penggunaan. Oleh karena itu, keamanan kriptografi tidak boleh dipandang sebagai kondisi final, melainkan sebagai proses berkelanjutan yang menuntut evaluasi kritis, pembaruan rutin, dan desain sistem yang fleksibel agar tetap tangguh menghadapi ancaman di masa depan.

---

## 9. Daftar Pustaka

- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography.*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit abc12345
Author: Subhan Susilo
Date:   2026-01-26

    week14-analisis-serangan: implementasi analisis-serangan dan laporan )
```

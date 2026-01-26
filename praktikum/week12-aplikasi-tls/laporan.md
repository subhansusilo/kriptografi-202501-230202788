# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan
- Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
- Menjelaskan enkripsi dalam transaksi e-commerce.
- Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

## 2. Dasar Teori

TLS (Transport Layer Security) pada E-commerce berfungsi sebagai mekanisme utama untuk mengamankan komunikasi antara pengguna dan server melalui proses enkripsi, autentikasi, dan penjagaan integritas data. Dengan penerapan TLS, informasi sensitif seperti username, password, alamat pelanggan, serta data pembayaran dapat terlindungi dari penyadapan dan manipulasi selama proses transmisi di jaringan. Selain itu, TLS membantu memastikan keaslian website E-commerce melalui sertifikat digital sehingga pengguna dapat memverifikasi bahwa mereka berinteraksi dengan situs yang sah, bukan situs palsu. Meskipun demikian, TLS bukanlah solusi keamanan yang bersifat menyeluruh, karena hanya melindungi data saat dikirimkan dan tidak secara langsung mencegah serangan lain seperti SQL Injection, malware, atau kebocoran data di sisi server. Oleh karena itu, penerapan TLS dalam E-commerce harus dikombinasikan dengan sistem keamanan lain, seperti pengamanan aplikasi, pengelolaan database yang aman, serta mekanisme proteksi pembayaran, agar tercipta sistem transaksi online yang aman dan terpercaya.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub    )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `sertifikat.png` di folder `praktikum/week12-aplikasi-tls/src/`.
2. Menyalin kode program dari panduan praktikum.

---

## 5. Source Code

---

## 6. Hasil dan Pembahasan

---

## 7. Jawaban Pertanyaan
- Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP (Hypertext Transfer Protocol) mengirimkan data dalam bentuk teks biasa (plaintext), sehingga informasi yang dikirimkan antara klien dan server dapat dengan mudah disadap atau dimodifikasi oleh pihak ketiga. Sebaliknya, HTTPS (Hypertext Transfer Protocol Secure) menggunakan TLS untuk mengenkripsi komunikasi, sehingga data menjadi tidak dapat dibaca oleh pihak yang tidak berwenang. Dengan HTTPS, selain kerahasiaan data terjaga, integritas informasi dan keaslian server juga dapat diverifikasi, sehingga HTTPS jauh lebih aman dan lebih dipercaya terutama untuk aplikasi yang melibatkan data sensitif seperti E-commerce dan perbankan digital.

- Sertifikat digital menjadi penting dalam komunikasi TLS karena berfungsi sebagai alat autentikasi yang memastikan identitas server yang diakses oleh pengguna. Sertifikat digital mengaitkan identitas suatu entitas dengan kunci publiknya dan dikeluarkan oleh Certificate Authority (CA) yang dipercaya. Tanpa sertifikat digital, proses enkripsi tetap dapat terjadi, tetapi pengguna tidak memiliki jaminan bahwa mereka benar-benar berkomunikasi dengan server yang sah, sehingga risiko serangan seperti man-in-the-middle dan phishing meningkat. Oleh karena itu, sertifikat digital tidak hanya mendukung keamanan teknis, tetapi juga membangun kepercayaan dalam komunikasi digital.

- Kriptografi mendukung privasi dalam komunikasi digital, karena memungkinkan data hanya dapat diakses oleh pihak yang memiliki kunci dekripsi yang sah, sehingga melindungi kerahasiaan informasi pribadi, komunikasi bisnis, dan transaksi keuangan. Namun, kekuatan kriptografi juga menimbulkan tantangan hukum dan etika, terutama ketika teknologi ini digunakan untuk menyembunyikan aktivitas ilegal atau menghambat penegakan hukum. Pemerintah dan aparat hukum sering menghadapi dilema antara melindungi hak privasi warga dan kebutuhan untuk melakukan pengawasan demi keamanan publik. Dengan demikian, kriptografi berada di titik konflik antara kebebasan individu dan kepentingan sosial, sehingga memerlukan regulasi dan kebijakan yang seimbang agar privasi tetap terjaga tanpa mengorbankan aspek hukum dan etika.

---

## 8. Kesimpulan
Secara keseluruhan, penerapan HTTPS dengan dukungan TLS dan sertifikat digital merupakan fondasi penting dalam keamanan komunikasi digital, terutama pada sistem yang melibatkan pertukaran data sensitif. Perbedaan antara HTTP dan HTTPS menunjukkan bahwa keamanan bukan sekadar fitur tambahan, melainkan kebutuhan utama untuk menjaga kerahasiaan, integritas, dan keaslian data. Sertifikat digital berperan krusial dalam membangun kepercayaan antara pengguna dan server, sementara kriptografi memungkinkan perlindungan privasi dalam skala besar. Namun, di sisi lain, penggunaan kriptografi yang kuat juga memunculkan tantangan hukum dan etika terkait pengawasan, penegakan hukum, dan penyalahgunaan teknologi. Oleh karena itu, keamanan komunikasi digital tidak hanya menuntut solusi teknis yang andal, tetapi juga keseimbangan kebijakan dan kesadaran etis agar perlindungan privasi dapat berjalan seiring dengan kepentingan hukum dan sosial.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Kahn Academy. *Cryptography: An Introduction*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit abc12345
Author: Subhan Susilo
Date:   2026-01-26

    week2-cryptosystem: implementasi Aplikasi TLS & E-commerce dan laporan )
```

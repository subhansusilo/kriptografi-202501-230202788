# Laporan Praktikum Kriptografi
Minggu ke-: 09  
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
- Memverifikasi keaslian tanda tangan digital.
- Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.


---

## 2. Dasar Teori
Tanda tangan digital adalah mekanisme kriptografi yang digunakan untuk menjamin keaslian (authenticity), integritas (integrity), dan non-repudiation (tidak bisa disangkal) suatu dokumen digital. Berbeda dari tanda tangan biasa, tanda tangan digital dibuat menggunakan kunci privat, diverifikasi menggunakan kunci publik, dan didukung oleh algoritma matematika yang kuat

Digital Signature dengan RSA
- RSA awalnya algoritma enkripsi, tapi juga bisa dipakai buat tanda tangan.
- Prosesnya: hash → ditandatangani pakai kunci privat → diverifikasi pakai kunci publik.
- Kelebihan: verifikasi cepat, konsep mudah dimengerti.

Digital Signature dengan DSA
- DSA memang khusus untuk tanda tangan digital.
- Menggunakan bilangan acak (nonce k) setiap kali menandatangani.
- Kelebihan: membuat tanda tangan lebih cepat.
- Kekurangan: kalau k bocor atau dipakai ulang, kunci privat bisa terbongkar.

Perbedaan RSA dan DSA 
- RSA: simpel, verifikasi cepat, tidak wajib pakai angka acak.
- DSA: tanda tangan cepat, tapi harus pakai angka acak unik (nonce).
- Keduanya sama-sama aman, hanya berbeda gaya dan karakteristik

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  )

---

## 4. Langkah Percobaan
1. Membuat file `signature.py` di folder `praktikum/week2-digital-signature/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python signature.py`.)

---

## 5. Source Code
Langkah 1 — Generate Key dan Buat Tanda Tangan

    from Crypto.PublicKey import RSA
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256
    
    # Generate pasangan kunci RSA
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    
    # Pesan yang akan ditandatangani
    message = b"Hello, ini pesan penting."
    h = SHA256.new(message)
    
    # Buat tanda tangan dengan private key
    signature = pkcs1_15.new(private_key).sign(h)
    print("Signature:", signature.hex())

Langkah 2 — Verifikasi Tanda Tangan
    
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("Verifikasi berhasil: tanda tangan valid.")
    except (ValueError, TypeError):
        print("Verifikasi gagal: tanda tangan tidak valid.")

Langkah 3 — Uji Modifikasi Pesan
    
    # Modifikasi pesan
    fake_message = b"Hello, ini pesan palsu."
    h_fake = SHA256.new(fake_message)
    
    try:
        pkcs1_15.new(public_key).verify(h_fake, signature)
        print("Verifikasi berhasil (seharusnya gagal).")
    except (ValueError, TypeError):
        print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")


---

## 6. Hasil dan Pembahasan

![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan

1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
Perbedaan utamanya ada pada arah penggunaan kunci dan tujuan prosesnya:
- Enkripsi RSA:
    - Pengirim mengenkripsi pesan dengan kunci publik penerima.
    - Penerima mendekripsi dengan kunci privatnya.
    - Tujuannya: menjaga kerahasiaan (confidentiality).
- Tanda Tangan Digital RSA:
    - Pengirim menandatangani hash pesan dengan kunci privatnya sendiri.
    - Orang lain memverifikasi dengan kunci publik pengirim.
    - Tujuannya: integritas, keaslian, dan non-repudiation.
  
Kesimpulan:
- Enkripsi = melindungi pesan.
- Tanda tangan digital = membuktikan siapa pengirimnya dan memastikan pesan tidak berubah.

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?

Tanda tangan digital memberi dua jaminan karena:

a) Integritas

Sebelum ditandatangani, pesan diubah menjadi hash.

Jika ada perubahan sekecil apa pun pada pesan:
- hash akan berubah total,
- verifikasi tanda tangan otomatis gagal.

Jadi, tanda tangan digital memberitahu jika pesan diubah.

b) Otentikasi

Tanda tangan dibuat memakai kunci privat pengirim, dan hanya ia yang memiliki kunci tersebut.

Siapa pun yang punya kunci publik pengirim bisa memverifikasi tanda tangan.

Kesimpulan:
- hanya pemilik kunci privat yang bisa membuat tanda tangan itu,
- sehingga penerima yakin pesan benar dari pengirim asli.

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?

Certificate Authority (CA) berfungsi sebagai pihak terpercaya yang memverifikasi identitas pemilik kunci publik.

CA mengeluarkan sertifikat digital, yang berisi:

- identitas pemilik (nama, organisasi, domain),
- kunci publik miliknya,
- tanda tangan CA sebagai bukti validitas.

Peran CA:

- Membuktikan bahwa kunci publik benar milik orang/organisasi tersebut.Tanpa CA, siapa pun bisa membuat kunci palsu.
- Mencegah serangan penyamaran (impersonation).
- Menjadi “trust anchor” dalam ekosistem keamanan (SSL/TLS, email, dokumen resmi, dsb).

Tanpa CA, tanda tangan digital tetap bekerja secara matematika, tapi kita tidak pernah tahu apakah kunci publik yang kita pakai itu benar milik orang yang kita maksud.

---

## 8. Kesimpulan
Tanda tangan digital adalah mekanisme kriptografi yang digunakan untuk memastikan bahwa sebuah pesan benar-benar berasal dari pengirimnya dan tidak mengalami perubahan. Berbeda dari enkripsi RSA yang bertujuan menjaga kerahasiaan data, tanda tangan digital RSA menggunakan arah kunci yang terbalik: kunci privat dipakai untuk menandatangani, sementara kunci publik digunakan untuk memverifikasi. Dengan pendekatan ini, tanda tangan digital dapat menjamin integritas (karena memanfaatkan hash yang berubah total jika pesan diubah) dan otentikasi (karena hanya pemilik kunci privat yang bisa membuat tanda tangan yang valid).

Dalam sistem modern, kepercayaan ini diperkuat oleh Certificate Authority (CA), yaitu lembaga terpercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital. Tanpa CA, pengguna tidak bisa memastikan apakah kunci publik yang digunakan benar-benar milik pihak yang sah. Karena itu, kombinasi tanda tangan digital dan CA menjadi fondasi penting dalam keamanan komunikasi digital di internet—mulai dari HTTPS, email, hingga dokumen resmi elektronik.

---

## 9. Daftar Pustaka
 
- Paar, C., & Pelzl, J. *Understanding Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit abc12345
Author: Subhan Susilo <subhansusilo04@gmail.coml>
Date:   2025-12-08

    week9-digital-signature: implementasi Digital Signaturer dan laporan )
```

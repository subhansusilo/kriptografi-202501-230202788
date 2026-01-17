# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
- Menjelaskan konsep Shamir Secret Sharing (SSS).
- Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
- Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Secret Sharing (Shamir’s Secret Sharing) adalah metode kriptografi untuk membagi sebuah rahasia (misalnya kunci enkripsi) menjadi beberapa bagian yang disebut shares, lalu mendistribusikannya ke banyak pihak. Rahasia hanya dapat direkonstruksi jika minimal sejumlah shares tertentu (ambang batas, k) digabungkan, sementara jumlah shares di bawah ambang batas tersebut tidak memberikan informasi apa pun tentang rahasia.

Skema ini diperkenalkan oleh Adi Shamir dan didasarkan pada sifat matematika polinomial: sebuah polinomial berderajat (k−1) ditentukan secara unik oleh k titik. Dengan demikian, sistem ini memberikan keamanan informasi-teoretis (bukan sekadar komputasional), sehingga cocok untuk melindungi rahasia penting dalam sistem terdistribusi, manajemen kunci, dan toleransi kegagalan

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub   )

---

## 4. Langkah Percobaan
1. Membuat file `secret_sharing.py` di folder `praktikum/week11-secret-sharing/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python secret_sharing.py`.)

---

## 5. Source Code
    from secretsharing import SecretSharer
    
    #Rahasia yang ingin dibagi
    
    secret = "KriptografiUPB2025"
    
    #Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
    
    shares = SecretSharer.split_secret(secret, 3, 5)
    
    print("Shares:", shares)
    
    #Rekonstruksi rahasia dari 3 shares
    
    recovered = SecretSharer.recover_secret(shares[:3])
    
    print("Recovered secret:", recovered)

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program secret_sharing:

![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
1. Keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci langsung
Keuntungan utamanya adalah penghapusan single point of failure.
Jika kunci dibagikan sebagai salinan utuh ke beberapa pihak, kebocoran satu pihak saja sudah cukup untuk membocorkan seluruh rahasia. Ini asumsi berbahaya yang sering dianggap “aman karena banyak orang pegang”.
Dalam Shamir’s Secret Sharing (SSS), tidak ada satu pun pihak yang memegang rahasia lengkap. Setiap share tidak bermakna secara kriptografis jika berdiri sendiri. Bahkan penyerang dengan komputasi tak terbatas tidak bisa menebak rahasia hanya dari share di bawah threshold. Ini memberi keamanan informasi-teoretis, bukan sekadar “sulit dipecahkan”.

2. Peran threshold (k) dalam keamanan secret sharing

Threshold (k) adalah parameter penentu keamanan dan ketersediaan.

- Keamanan

Selama penyerang hanya memiliki < k share, informasi tentang rahasia = nol. Tidak ada “sedikit bocor”. Ini sering disalahpahami, padahal             justru kekuatan utama SSS.

- Ketersediaan (availability)

Threshold memungkinkan sistem tetap berfungsi meski beberapa pihak gagal, hilang, atau tidak kooperatif. Tidak semua pemegang share harus          hadir.

3. Shamir’s Secret Sharing sangat bermanfaat dalam manajemen kunci master pada organisasi atau infrastruktur kritis, misalnya untuk melindungi kunci utama akses sistem cadangan data nasional, kunci privat Certificate Authority (CA), atau recovery key pada cold wallet cryptocurrency milik perusahaan. Dalam skema ini, satu kunci rahasia dibagi menjadi lima share dengan threshold k = 3, sehingga rahasia hanya dapat direkonstruksi jika minimal tiga share digabungkan. Setiap share disimpan oleh pihak yang berbeda, seperti Direktur IT, auditor internal, legal officer, lokasi cadangan offsite, dan Hardware Security Module (HSM). Dengan pengaturan ini, tidak ada satu individu pun yang dapat menyalahgunakan kunci secara sepihak, sementara organisasi tetap mampu memulihkan akses meskipun satu atau dua pihak tidak tersedia. Pendekatan ini secara signifikan meningkatkan ketahanan terhadap kegagalan dan serangan internal, dan skema tersebut pertama kali diformalkan oleh Adi Shamir, yang hingga kini masih dianggap sebagai standar emas dalam distribusi rahasia bernilai tinggi.

---

## 8. Kesimpulan
Shamir’s Secret Sharing (SSS) adalah cara membagi kunci/rahasia menjadi beberapa share sehingga rahasia hanya bisa dipulihkan jika memenuhi ambang minimal (threshold k). Dibanding membagikan salinan kunci utuh, SSS menghilangkan risiko kebocoran dari satu pihak karena share di bawah threshold tidak mengungkap apa pun tentang rahasia. Dengan memilih nilai k yang tepat, organisasi mendapat dua keuntungan sekaligus: keamanan lebih kuat (mengurangi penyalahgunaan/kolusi internal) dan ketersediaan lebih baik (tetap bisa recovery meski 1–2 pihak tidak tersedia), sehingga sangat cocok untuk pengelolaan kunci bernilai tinggi seperti akses backup kritis, kunci privat CA, atau recovery key cold wallet.

---

## 9. Daftar Pustaka
  
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. *Handbook of Applied Cryptography. CRC Press*.  
- Katz, J., & Lindell, Y. *Katz, J., & Lindell, Y.*.  

---

## 10. Commit Log

```
commit 26247326c5992285629b63957a98eafa15da6e31
Author: Subhan Susilo <email>
Date:   2026-01-17

    week11-secret-sharing: implementasi Secret Sharing dan laporan )
```

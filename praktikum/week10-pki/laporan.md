# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Membuat sertifikat digital sederhana.
- Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
- Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).


---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah kerangka kerja keamanan yang digunakan untuk mengelola kriptografi kunci publik guna menjamin keamanan komunikasi digital. PKI bekerja dengan sepasang kunci, yaitu kunci publik dan kunci privat, yang digunakan untuk enkripsi, autentikasi, dan menjaga integritas data. Melalui PKI, identitas pengguna, sistem, atau organisasi dapat dikaitkan secara aman dengan kunci publik menggunakan sertifikat digital.

Sertifikat digital diterbitkan dan diverifikasi oleh Certificate Authority (CA), yaitu pihak ketiga yang dipercaya untuk memastikan keaslian identitas pemilik sertifikat. CA menandatangani sertifikat secara digital sehingga pihak lain dapat memercayai kunci publik yang digunakan. Dalam praktiknya, CA disusun dalam struktur hirarki seperti Root CA dan Intermediate CA yang membentuk rantai kepercayaan (chain of trust).

PKI banyak digunakan dalam berbagai layanan digital, seperti HTTPS pada website, pengamanan email, VPN, dan tanda tangan digital. Dengan adanya PKI dan CA, komunikasi digital menjadi lebih aman, terpercaya, dan dapat dipertanggungjawabkan, meskipun pengelolaannya membutuhkan sistem dan kontrol keamanan yang baik.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat file `pki_cert.py` di folder `praktikum/week10-pki/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python pki_cert.py`.

---

## 5. Source Code
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from datetime import datetime, timedelta
    
    # Generate key pair
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    # Buat subject & issuer (CA sederhana = self-signed)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
    ])

    # Buat sertifikat
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .sign(key, hashes.SHA256())
    )
    
    # Simpan sertifikat
    with open("cert.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    print("Sertifikat digital berhasil dibuat: cert.pem")

---

## 6. Hasil dan Pembahasan

Hasil eksekusi program pki_cert:

![Hasil Eksekusi](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
1. Apa fungsi utama Certificate Authority (CA)?
Fungsi utama Certificate Authority (CA) adalah memverifikasi identitas pemilik sertifikat digital dan menerbitkan sertifikat yang tepercaya. CA menjamin bahwa kunci publik dalam sertifikat benar-benar milik pihak yang sah, sehingga pengguna lain dapat mempercayai komunikasi yang dilakukan.

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Self-signed certificate tidak cukup untuk sistem produksi karena tidak diverifikasi oleh pihak tepercaya. Sertifikat ini mudah dipalsukan dan akan menimbulkan peringatan keamanan pada browser atau aplikasi, sehingga tidak memberikan jaminan keaslian identitas dan berisiko terhadap serangan keamanan.

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan Man-in-the-Middle (MITM) dengan cara memverifikasi sertifikat server melalui CA tepercaya. Jika sertifikat tidak valid atau dipalsukan, koneksi akan ditolak. Dengan begitu, klien hanya berkomunikasi dengan server yang identitasnya telah dipastikan asli dan terpercaya.
---

## 8. Kesimpulan
Public Key Infrastructure (PKI) dan Certificate Authority (CA) merupakan fondasi utama dalam keamanan komunikasi digital. PKI menyediakan mekanisme pengelolaan kunci publik dan sertifikat digital, sementara CA berperan sebagai pihak tepercaya yang memverifikasi identitas dan menjamin keaslian sertifikat. Melalui proses ini, PKI mampu memastikan kerahasiaan, keaslian, dan integritas data dalam komunikasi seperti TLS/HTTPS. Tanpa CA yang tepercaya dan pengelolaan PKI yang baik, sistem produksi akan rentan terhadap ancaman seperti pemalsuan identitas dan serangan Man-in-the-Middle, sehingga keamanan dan kepercayaan dalam pertukaran data digital tidak dapat terjamin.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Rescorla, E *The Transport Layer Security (TLS) Protocol Version*.  
- Green, M., & Smith, J. *Cryptography Engineering*.  )

---

## 10. Commit Log

```
commit abc12345
Author: SubhanSusilo <subhansusilo4@gmail.com>
Date:   2025-12-20

    week10-pki: implementasi pki_cert dan laporan )
```

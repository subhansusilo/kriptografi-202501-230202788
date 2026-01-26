# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Subhan Susilo]  
NIM: [230202788]  
Kelas: [5IKRA]  

---

## 1. Tujuan

- Menjelaskan peran hash function dalam blockchain.
- Melakukan simulasi sederhana Proof of Work (PoW).
- Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
 
TinyChain dengan mekanisme Proof of Work (PoW) merupakan model blockchain sederhana yang dirancang untuk tujuan pembelajaran, khususnya untuk memahami konsep dasar bagaimana sebuah blockchain bekerja. Dalam TinyChain, Proof of Work berfungsi sebagai mekanisme validasi blok, di mana setiap blok baru hanya dapat ditambahkan ke dalam rantai jika telah melalui proses komputasi tertentu. Proses ini dilakukan dengan cara mencari nilai nonce yang, ketika digabungkan dengan data blok dan hash blok sebelumnya lalu diproses menggunakan fungsi hash (misalnya SHA-256), menghasilkan hash yang memenuhi tingkat kesulitan tertentu, seperti diawali oleh sejumlah nol. Mekanisme ini bersifat trial and error, sehingga membutuhkan waktu dan sumber daya komputasi untuk menemukan hash yang valid.

Konsep utama yang ingin ditunjukkan oleh Proof of Work dalam TinyChain bukan sekadar membuat hash yang sulit, melainkan menciptakan kondisi di mana pembuatan blok menjadi mahal secara komputasi, tetapi sangat mudah untuk diverifikasi oleh pihak lain. Ketika sebuah blok berhasil ditambang, node lain cukup melakukan satu kali perhitungan hash untuk memastikan bahwa blok tersebut valid. Inilah yang membuat blockchain menjadi sulit untuk dimanipulasi, karena perubahan pada satu blok akan mengubah hash-nya dan memaksa penyerang untuk menghitung ulang blok tersebut beserta seluruh blok setelahnya.

Namun demikian, perlu disadari bahwa TinyChain dengan PoW hanya merepresentasikan konsep dasar dan bukan implementasi blockchain yang sepenuhnya realistis. TinyChain tidak melibatkan jaringan terdistribusi yang kompleks, kompetisi antar miner yang sesungguhnya, maupun insentif ekonomi seperti pada blockchain publik semacam Bitcoin. Selain itu, mekanisme Proof of Work sendiri memiliki keterbatasan, terutama dari sisi efisiensi energi dan potensi serangan apabila satu pihak menguasai sebagian besar kekuatan komputasi. Oleh karena itu, TinyChain sebaiknya dipahami sebagai alat bantu konseptual untuk mempelajari prinsip keamanan dan imutabilitas blockchain, bukan sebagai solusi siap pakai untuk sistem terdistribusi skala besar.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `tinychain.py` di folder `praktikum/week13-tinychain/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python tinychain.py`.)

---

## 5. Source Code
Langkah 1 — Membuat Struktur Blok
    import hashlib
    import time
    
    class Block:
        def __init__(self, index, previous_hash, data, timestamp=None):
            self.index = index
            self.timestamp = timestamp or time.time()
            self.data = data
            self.previous_hash = previous_hash
            self.nonce = 0
            self.hash = self.calculate_hash()
    
        def calculate_hash(self):
            value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
            return hashlib.sha256(value.encode()).hexdigest()
    
        def mine_block(self, difficulty):
            while self.hash[:difficulty] != "0" * difficulty:
                self.nonce += 1
                self.hash = self.calculate_hash()
            print(f"Block mined: {self.hash}")

Langkah 2 — Membuat Blockchain
    class Blockchain:
        def __init__(self):
            self.chain = [self.create_genesis_block()]
            self.difficulty = 4
    
        def create_genesis_block(self):
            return Block(0, "0", "Genesis Block")
    
        def get_latest_block(self):
            return self.chain[-1]
    
        def add_block(self, new_block):
            new_block.previous_hash = self.get_latest_block().hash
            new_block.mine_block(self.difficulty)
            self.chain.append(new_block)
    
    # Uji coba blockchain
    my_chain = Blockchain()
    print("Mining block 1...")
    my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))
    
    print("Mining block 2...")
    my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))

---

## 6. Hasil dan Pembahasan


---

## 7. Jawaban Pertanyaan

Fungsi hash sangat penting dalam blockchain karena berperan sebagai fondasi utama keamanan dan integritas data. Fungsi hash mengubah data dengan ukuran berapa pun menjadi keluaran dengan panjang tetap yang bersifat unik, sehingga perubahan sekecil apa pun pada data akan menghasilkan hash yang sangat berbeda. Sifat ini memungkinkan blockchain mendeteksi manipulasi data secara langsung, karena setiap blok menyimpan hash dari blok sebelumnya. Jika satu blok diubah, maka hash-nya berubah dan memutus keterkaitan dengan blok berikutnya, sehingga rantai menjadi tidak valid. Selain itu, fungsi hash bersifat satu arah (one-way function), artinya sangat sulit untuk menebak data asli hanya dari nilai hash, sehingga mendukung keamanan dan keandalan sistem blockchain.

Proof of Work mencegah terjadinya double spending dengan cara memaksa seluruh jaringan untuk menyepakati satu versi transaksi yang sah melalui proses komputasi yang mahal. Setiap transaksi yang telah dimasukkan ke dalam sebuah blok harus melalui proses mining dan kemudian divalidasi oleh mayoritas node di jaringan. Untuk melakukan double spending, penyerang harus membuat versi blockchain alternatif yang menghapus atau menggandakan transaksi tertentu dan sekaligus menambang ulang blok tersebut hingga menjadi rantai terpanjang. Hal ini membutuhkan kekuatan komputasi yang sangat besar dan biaya tinggi, sehingga secara praktis menjadi tidak masuk akal bagi sebagian besar penyerang. Dengan demikian, PoW tidak menghilangkan kemungkinan double spending secara absolut, tetapi membuatnya sangat mahal dan sulit dilakukan.

Kelemahan utama Proof of Work dalam hal efisiensi energi terletak pada sifat komputasinya yang berbasis percobaan berulang tanpa menghasilkan manfaat lain selain keamanan jaringan. Proses mining mengharuskan ribuan hingga jutaan perhitungan hash dilakukan hanya untuk menemukan satu nilai nonce yang valid, sementara sebagian besar perhitungan tersebut akhirnya terbuang sia-sia. Semakin tinggi tingkat kesulitan jaringan, semakin besar pula konsumsi energi yang dibutuhkan. Kondisi ini menimbulkan kritik karena PoW dianggap boros energi dan kurang ramah lingkungan, terutama ketika diterapkan pada blockchain berskala besar. Inilah alasan mengapa banyak sistem blockchain modern mulai mengeksplorasi mekanisme konsensus alternatif yang lebih efisien, seperti Proof of Stake.

---

## 8. Kesimpulan

Secara keseluruhan, blockchain mengandalkan fungsi hash dan mekanisme Proof of Work untuk menjaga keamanan, integritas, dan kepercayaan dalam sistem yang terdesentralisasi. Fungsi hash memastikan bahwa data di dalam blockchain bersifat konsisten dan sulit dimanipulasi, karena setiap perubahan dapat terdeteksi dengan mudah melalui perbedaan nilai hash. Sementara itu, Proof of Work berperan dalam mencegah kecurangan seperti double spending dengan cara membuat proses penambahan dan pengubahan blok menjadi sangat mahal secara komputasi, sehingga hanya transaksi yang telah diverifikasi oleh mayoritas jaringan yang dapat dianggap sah. Namun, meskipun efektif dari sisi keamanan, Proof of Work memiliki kelemahan signifikan dalam hal efisiensi energi karena membutuhkan daya komputasi besar dengan banyak proses yang tidak menghasilkan nilai tambah lain. Oleh sebab itu, Proof of Work cocok dipahami sebagai solusi keamanan yang kuat namun memiliki trade-off, sehingga mendorong munculnya mekanisme konsensus alternatif yang lebih efisien dan berkelanjutan.

---

## 9. Daftar Pustaka

- Antonopoulos, A. M.. *Mastering Bitcoin: Programming the Open Blockchain*.  
- Nakamoto, S. *Bitcoin: A Peer-to-Peer Electronic Cash System.*.  )

---

## 10. Commit Log

```
commit abc12345
Author: Subhan Susilo
Date:   2026-10-26

    week13-tinychain: implementasi tinychain dan laporan )
```

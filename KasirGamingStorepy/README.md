# 🕹️ Nexus Gaming Store – Python Cashier System (CLI)

**Nexus Gaming Store** adalah aplikasi **mesin kasir berbasis Python (CLI)** yang dirancang sebagai **Sistem Informasi Penjualan** untuk toko gaming & komponen PC.  
Aplikasi ini mampu mengelola transaksi penjualan, mencetak struk, menyimpan data transaksi, serta menghasilkan laporan pendapatan harian.

Project ini dibuat **tanpa framework tambahan**, hanya menggunakan **Python standard library**, sehingga mudah dijalankan dan dipahami.

---

## 📌 Fitur Utama

- 🔐 Login kasir (nama bebas)
- 🗂️ Kategori produk & stok barang
- 🛒 Multi-produk dalam satu transaksi
- 🧾 Nomor transaksi otomatis
- 🖨️ Struk ditampilkan di terminal
- 💾 Struk disimpan ke file `.txt`
- 📊 Transaksi disimpan ke file `.csv`
- 📈 Laporan pendapatan harian
- 🔁 Multi transaksi tanpa restart aplikasi

---

## 🧠 Konsep Sistem Informasi

Aplikasi ini memenuhi konsep dasar **Sistem Informasi**:

| Komponen | Implementasi |
|--------|-------------|
| Input  | Produk, jumlah beli, pembayaran |
| Proses | Perhitungan total, stok, transaksi |
| Output | Struk, laporan pendapatan |
| Storage | CSV (data transaksi), TXT (struk) |
| Informasi | Total pendapatan harian |

---

## 📂 Struktur File

```text
KasirGamingStorepy/
│
├── python_kasir_gaming_store.py   # File utama program
├── transaksi.csv                 # Data transaksi (auto-generated)
├── struk_TRX-YYYYMMDD-XXXX.txt   # Struk transaksi (auto-generated)
└── README.md
```

---

## ▶️ Cara Menjalankan Program
1. Pastikan Python Terinstall

Minimal Python 3.9+

Cek versi:

```bash
python --version
```

2. Jalankan Program

```bash
python python_kasir_gaming_store.py
```

---

## 🖥️ Contoh Alur Penggunaan

1. Login kasir (nama bebas)

2. Pilih kategori produk

3. Pilih produk & jumlah

4. Selesaikan belanja

5. Masukkan nominal pembayaran

6. Struk tampil di terminal

7. Struk otomatis tersimpan ke .txt

8. Data transaksi tersimpan ke .csv

9. Sistem siap untuk transaksi berikutnya

---

## 🧾 Contoh Struk (Terminal)

```text
           NEXUS GAMING STORE
      Jl. Teknologi No. 99, Jakarta
          Telp: 0812-3456-7890
========================================
No Transaksi : TRX-20260202-0001
Kasir        : Riyan
02-02-2026 13:42
========================================
Processor Ryzen 7 5800X x1  Rp3,800,000
RTX 3070 8GB            x1  Rp7,600,000
Monitor 24" 144Hz       x1  Rp2,800,000
========================================
TOTAL                Rp14,200,000
BAYAR                Rp15,000,000
KEMBALIAN              Rp800,000
========================================
              TERIMA KASIH
             KEEP GAMING 🎮
```

---

## 📊 Format File Transaksi (transaksi.csv)

```text
no_transaksi,tanggal,kasir,produk,qty,total
TRX-20260202-0001,2026-02-02,Riyan,RTX 3070 8GB,1,7600000
```

---

## ⚙️ Teknologi yang Digunakan

- Python 3

- CSV (data storage)

- TXT (struk transaksi)

- Standard Library:

    - datetime

    - csv

    - os

---

## 🚀 Pengembangan Selanjutnya (Opsional)

- Laporan penjualan per kasir

- Laporan per kategori produk

- Warning stok menipis

- Diskon & pajak (PPN)

- Warna terminal (ANSI)

- Export laporan bulanan

---

## 👨‍💻 Author

Riyan
Project Sistem Informasi – Python CLI
2026

---

## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan akademik.
Bebas dikembangkan dan dimodifikasi.
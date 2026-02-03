# 🏛️ Sistem Informasi Inventaris & Peminjaman  
## Laboratorium Fakultas Teknik (Python CLI)

Sistem Informasi Inventaris & Peminjaman Alat Laboratorium Fakultas Teknik adalah aplikasi **berbasis Python (Command Line Interface)** yang digunakan untuk mengelola **aset laboratorium lintas jurusan**, proses **peminjaman dan pengembalian alat**, serta **perhitungan denda keterlambatan**.

Aplikasi ini dirancang menggunakan **1 file Python** dengan penyimpanan data berbasis **CSV**, sehingga ringan, mudah dipahami, dan cocok untuk keperluan **pembelajaran Sistem Informasi**.

---

## 🎯 Tujuan Sistem
- Mengelola data inventaris alat laboratorium Fakultas Teknik
- Mengontrol ketersediaan alat lintas jurusan
- Mencatat transaksi peminjaman & pengembalian
- Menghitung denda keterlambatan secara otomatis
- Menyediakan laporan denda sebagai informasi pengambilan keputusan

---

## 🧠 Konsep Sistem Informasi
Sistem ini menerapkan konsep dasar **Sistem Informasi**:

| Komponen | Implementasi |
|--------|--------------|
| Input | Data alat, peminjam, lama pinjam |
| Proses | Validasi stok, perhitungan jatuh tempo & denda |
| Output | Bukti pengembalian, laporan denda |
| Storage | File CSV (inventaris & peminjaman) |
| Informasi | Status alat, total denda |

---

## 🏫 Cakupan Jurusan (Urutan E.S.P.I.I.M.A.SI)
Inventaris disusun berdasarkan urutan jurusan Fakultas Teknik:

1. **E**lektro  
2. **S**ipil  
3. **P**WK  
4. **I**ndustri  
5. **I**T (Informatika)  
6. **M**esin  
7. **A**rsitektur  
8. **SI** (Sistem Informasi)

Setiap jurusan memiliki **alat laboratorium yang realistis dan relevan** dengan bidang keilmuannya.

---

## ✨ Fitur Utama

### 🔐 Login Petugas
- Nama petugas bebas
- Dicatat pada setiap transaksi peminjaman & pengembalian

### 📦 Manajemen Inventaris
- Data alat per jurusan
- Stok tersedia & total
- Update stok otomatis saat pinjam/kembali

### 🔄 Peminjaman Alat
- Nomor peminjaman otomatis (`INV-YYYYMMDD-XXXX`)
- Data peminjam (Nama & NIM/NIP)
- Lama pinjam (hari)
- Status peminjaman

### 🔁 Pengembalian Alat
- Validasi nomor peminjaman
- Perhitungan hari keterlambatan
- Update status & stok otomatis
- **Bukti pengembalian ditampilkan di terminal**

### 💸 Denda Keterlambatan
- **Rp300.000 / hari / alat**
- Dihitung otomatis
- Tercatat dalam sistem

### 📊 Laporan
- Total denda terkumpul
- Data diambil langsung dari transaksi (CSV)

---

## 🧾 Bukti Pengembalian
Saat pengembalian berhasil, sistem akan:
- Menampilkan **Bukti Pengembalian** di terminal
- Menyimpan bukti ke file `.txt`

Contoh informasi bukti:
- Nomor peminjaman
- Data peminjam
- Alat & jumlah
- Tanggal pinjam, jatuh tempo, kembali
- Hari telat
- Total denda
- Nama petugas

---

## 📂 Struktur File

```text
inventory_lab_ft.py   # Program utama (1 file Python)
inventaris.csv        # Data inventaris (auto-generate)
peminjaman.csv        # Data peminjaman & pengembalian (auto-generate)
bukti_INV-*.txt       # Bukti pengembalian
README.md
```

---

## ▶️ Cara Menjalankan Program
### 1️⃣ Pastikan Python Terinstall

Minimal Python 3.9+

Cek versi:

```bash
python --version
```

### 2️⃣ Jalankan Program

```bash
python inventory_lab_ft.py
```

---

## ⚙️ Teknologi yang Digunakan

- Python 3

- CSV file storage

- Standard Library:

    - csv

    - os

    - datetime

---

## 🚀 Pengembangan Selanjutnya (Opsional)

- Laporan per jurusan

- Riwayat peminjaman per mahasiswa

- Grafik laporan (ASCII)

- Hak akses multi petugas

- Export laporan bulanan

---

## 👨‍💻 Author

Made by Riyan -
Project Sistem Informasi
Fakultas Teknik
2026

---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran.
Bebas digunakan, dimodifikasi, dan dikembangkan lebih lanjut.
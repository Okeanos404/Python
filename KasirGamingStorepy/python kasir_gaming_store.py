import datetime
import csv
import os

# ======================
# IDENTITAS TOKO
# ======================
NAMA_TOKO = "NEXUS GAMING STORE"
ALAMAT_TOKO = "Jl. Teknologi No. 99, Jakarta"
TELP_TOKO = "0812-3456-7890"
LEBAR_STRUK = 40

# ======================
# DATA PRODUK
# ======================
produk = {
    "Komponen PC": [
        {"kode": "PC01", "nama": "Processor Ryzen 5 5600X", "harga": 2800000, "stok": 5},
        {"kode": "PC02", "nama": "Processor Ryzen 7 5800X", "harga": 3800000, "stok": 4},
        {"kode": "PC03", "nama": "Processor Intel i5 12400F", "harga": 2600000, "stok": 6},
        {"kode": "PC04", "nama": "Processor Intel i7 12700F", "harga": 4200000, "stok": 3},
        {"kode": "PC05", "nama": "Motherboard B550", "harga": 2100000, "stok": 6},
        {"kode": "PC06", "nama": "Motherboard B660", "harga": 2300000, "stok": 5},
        {"kode": "PC07", "nama": "RAM DDR4 8GB", "harga": 450000, "stok": 25},
        {"kode": "PC08", "nama": "RAM DDR4 16GB", "harga": 850000, "stok": 15},
        {"kode": "PC09", "nama": "SSD NVMe 512GB", "harga": 750000, "stok": 18},
        {"kode": "PC10", "nama": "SSD NVMe 1TB", "harga": 1300000, "stok": 12},
        {"kode": "PC11", "nama": "HDD 1TB", "harga": 650000, "stok": 10},
        {"kode": "PC12", "nama": "Power Supply 650W", "harga": 950000, "stok": 8},
        {"kode": "PC13", "nama": "Power Supply 750W Gold", "harga": 1400000, "stok": 6},
        {"kode": "PC14", "nama": "Casing ATX RGB", "harga": 850000, "stok": 10},
        {"kode": "PC15", "nama": "CPU Cooler Tower", "harga": 450000, "stok": 14},
    ],

    "VGA / GPU": [
        {"kode": "VG01", "nama": "RTX 3060 12GB", "harga": 5200000, "stok": 4},
        {"kode": "VG02", "nama": "RTX 3070 8GB", "harga": 7600000, "stok": 3},
        {"kode": "VG03", "nama": "RTX 3080 10GB", "harga": 9800000, "stok": 2},
        {"kode": "VG04", "nama": "RTX 4060 8GB", "harga": 5900000, "stok": 5},
        {"kode": "VG05", "nama": "RX 6600 XT", "harga": 4800000, "stok": 6},
        {"kode": "VG06", "nama": "RX 6700 XT", "harga": 6500000, "stok": 4},
        {"kode": "VG07", "nama": "RX 7600", "harga": 5200000, "stok": 5},
    ],

    "Mouse Gaming": [
        {"kode": "MS01", "nama": "Logitech G102", "harga": 250000, "stok": 30},
        {"kode": "MS02", "nama": "Logitech G304", "harga": 450000, "stok": 20},
        {"kode": "MS03", "nama": "Logitech G Pro X", "harga": 1500000, "stok": 6},
        {"kode": "MS04", "nama": "Razer DeathAdder", "harga": 450000, "stok": 18},
        {"kode": "MS05", "nama": "Razer Viper Mini", "harga": 380000, "stok": 15},
        {"kode": "MS06", "nama": "SteelSeries Rival 3", "harga": 550000, "stok": 12},
        {"kode": "MS07", "nama": "Fantech UX1", "harga": 180000, "stok": 40},
        {"kode": "MS08", "nama": "Glorious Model O", "harga": 900000, "stok": 8},
    ],

    "Keyboard Gaming": [
        {"kode": "KB01", "nama": "Mechanical Red Switch", "harga": 600000, "stok": 15},
        {"kode": "KB02", "nama": "Mechanical Blue Switch", "harga": 650000, "stok": 12},
        {"kode": "KB03", "nama": "Mechanical Brown Switch", "harga": 700000, "stok": 10},
        {"kode": "KB04", "nama": "RGB Gaming Keyboard", "harga": 750000, "stok": 14},
        {"kode": "KB05", "nama": "Keyboard Office", "harga": 150000, "stok": 30},
        {"kode": "KB06", "nama": "Keychron K2 Wireless", "harga": 1500000, "stok": 6},
        {"kode": "KB07", "nama": "Royal Kludge RK61", "harga": 650000, "stok": 12},
    ],

    "Headset & Audio": [
        {"kode": "HS01", "nama": "Headset HyperX Cloud", "harga": 900000, "stok": 8},
        {"kode": "HS02", "nama": "Razer Kraken", "harga": 1200000, "stok": 6},
        {"kode": "HS03", "nama": "SteelSeries Arctis 3", "harga": 1100000, "stok": 5},
        {"kode": "HS04", "nama": "Gaming Earphone", "harga": 350000, "stok": 25},
        {"kode": "HS05", "nama": "Headphone Studio", "harga": 850000, "stok": 10},
        {"kode": "HS06", "nama": "USB Condenser Mic", "harga": 750000, "stok": 7},
    ],

    "Monitor & Aksesoris": [
        {"kode": "MN01", "nama": "Monitor 24\" 144Hz", "harga": 2800000, "stok": 6},
        {"kode": "MN02", "nama": "Monitor 27\" IPS", "harga": 3500000, "stok": 4},
        {"kode": "MN03", "nama": "Monitor 34\" Ultrawide", "harga": 6500000, "stok": 2},
        {"kode": "AK01", "nama": "Mousepad Gaming XL", "harga": 150000, "stok": 40},
        {"kode": "AK02", "nama": "Webcam HD", "harga": 450000, "stok": 12},
        {"kode": "AK03", "nama": "USB Hub", "harga": 120000, "stok": 30},
        {"kode": "AK04", "nama": "Controller Gamepad", "harga": 350000, "stok": 15},
    ]
}

# ======================
# FILE CSV
# ======================
FILE_CSV = "transaksi.csv"

if not os.path.exists(FILE_CSV):
    with open(FILE_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["no_transaksi", "tanggal", "kasir", "produk", "qty", "total"])

# ======================
# LOGIN KASIR
# ======================
def login_kasir():
    print("=== LOGIN KASIR ===")
    while True:
        kasir = input("Masukkan nama kasir: ").strip()
        if kasir:
            print(f"✅ Kasir aktif: {kasir}\n")
            return kasir

# ======================
# NOMOR TRANSAKSI
# ======================
def generate_no_transaksi():
    today = datetime.date.today().strftime("%Y%m%d")
    count = 1
    if os.path.exists(FILE_CSV):
        with open(FILE_CSV, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["no_transaksi"].startswith(f"TRX-{today}"):
                    count += 1
    return f"TRX-{today}-{count:04d}"

# ======================
# TAMPILAN
# ======================
def tampil_kategori():
    print("\n=== KATEGORI PRODUK ===")
    for i, k in enumerate(produk.keys(), 1):
        print(f"{i}. {k}")
    print("0. Selesai Belanja")

def tampil_produk(kategori):
    print(f"\n--- {kategori.upper()} ---")
    for i, p in enumerate(produk[kategori], 1):
        print(f"{i}. {p['nama']} | Rp{p['harga']:,} | Stok: {p['stok']}")

# ======================
# STRUK (TERMINAL + TXT)
# ======================
def cetak_struk(no_trx, kasir, keranjang, total, bayar, kembali):
    lines = []
    center = lambda t: t.center(LEBAR_STRUK)
    garis = "=" * LEBAR_STRUK

    lines.append(center(NAMA_TOKO))
    lines.append(center(ALAMAT_TOKO))
    lines.append(center(f"Telp: {TELP_TOKO}"))
    lines.append(garis)
    lines.append(f"No Transaksi : {no_trx}")
    lines.append(f"Kasir        : {kasir}")
    lines.append(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    lines.append(garis)

    for item in keranjang:
        nama = item["nama"][:20]
        qty = item["qty"]
        subtotal = f"Rp{item['total']:,}"
        lines.append(f"{nama:<20} x{qty:<3} {subtotal:>10}")

    lines.append(garis)
    lines.append(f"{'TOTAL':<20} Rp{total:,}")
    lines.append(f"{'BAYAR':<20} Rp{bayar:,}")
    lines.append(f"{'KEMBALIAN':<20} Rp{kembali:,}")
    lines.append(garis)
    lines.append(center("TERIMA KASIH"))
    lines.append(center("KEEP GAMING 🎮"))

    # TAMPIL DI TERMINAL
    print("\n" + "\n".join(lines) + "\n")

    # SIMPAN KE FILE
    nama_file = f"struk_{no_trx}.txt"
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"🧾 Struk disimpan: {nama_file}")

def simpan_csv(no_trx, kasir, keranjang):
    with open(FILE_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        for item in keranjang:
            writer.writerow([
                no_trx,
                datetime.date.today(),
                kasir,
                item["nama"],
                item["qty"],
                item["total"]
            ])

def laporan_harian():
    total = 0
    today = str(datetime.date.today())
    with open(FILE_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["tanggal"] == today:
                total += int(row["total"])
    print(f"📊 TOTAL PENDAPATAN HARI INI: Rp{total:,}")

# ======================
# PROGRAM UTAMA
# ======================
kasir_aktif = login_kasir()

while True:
    keranjang = []

    while True:
        tampil_kategori()
        pilih = input("Pilih kategori: ")

        if pilih == "0":
            break

        kategori_list = list(produk.keys())
        if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(kategori_list):
            print("❌ Pilihan tidak valid")
            continue

        kategori = kategori_list[int(pilih) - 1]
        tampil_produk(kategori)

        idx = int(input("Pilih produk: ")) - 1
        barang = produk[kategori][idx]

        qty = int(input("Jumlah beli: "))
        if qty <= 0 or qty > barang["stok"]:
            print("❌ Stok tidak cukup")
            continue

        barang["stok"] -= qty
        keranjang.append({
            "nama": barang["nama"],
            "qty": qty,
            "total": barang["harga"] * qty
        })

        print("✅ Produk ditambahkan")

    if keranjang:
        total = sum(i["total"] for i in keranjang)
        print(f"\nTOTAL BELANJA: Rp{total:,}")

        while True:
            bayar = int(input("UANG BAYAR: Rp"))
            if bayar >= total:
                break
            print("❌ Uang kurang")

        kembali = bayar - total
        no_trx = generate_no_transaksi()

        simpan_csv(no_trx, kasir_aktif, keranjang)
        cetak_struk(no_trx, kasir_aktif, keranjang, total, bayar, kembali)

    laporan_harian()

    lanjut = input("\nTransaksi baru? (y/n): ")
    if lanjut.lower() != "y":
        print("Kasir ditutup.")
        break

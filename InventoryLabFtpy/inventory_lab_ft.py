import csv
import os
import datetime

# ======================
# KONFIGURASI
# ======================
NAMA_SISTEM = "SISTEM INVENTARIS LAB FAKULTAS TEKNIK"
DENDA_PER_HARI = 300000
LEBAR = 70

FILE_INVENTARIS = "inventaris.csv"
FILE_PEMINJAMAN = "peminjaman.csv"

# ======================
# DATA INVENTARIS AWAL
# URUTAN: E.S.P.I.I.M.A.SI
# ======================
inventaris_awal = [

    # ================= ELEKTRO =================
    ("LAB-EL-001", "Oscilloscope Digital", "Elektro", 5),
    ("LAB-EL-002", "Multimeter Digital", "Elektro", 20),
    ("LAB-EL-003", "Power Supply DC", "Elektro", 15),
    ("LAB-EL-004", "Signal Generator", "Elektro", 6),
    ("LAB-EL-005", "Trainer PLC", "Elektro", 4),

    # ================= SIPIL =================
    ("LAB-SP-001", "Theodolite", "Sipil", 5),
    ("LAB-SP-002", "Total Station", "Sipil", 3),
    ("LAB-SP-003", "Concrete Compression Tester", "Sipil", 2),
    ("LAB-SP-004", "Soil Compaction Tool", "Sipil", 6),
    ("LAB-SP-005", "Waterpass", "Sipil", 10),

    # ================= PWK =================
    ("LAB-PWK-001", "GPS Survey", "PWK", 8),
    ("LAB-PWK-002", "Drone Mapping", "PWK", 3),
    ("LAB-PWK-003", "Range Finder", "PWK", 6),
    ("LAB-PWK-004", "Peta Topografi", "PWK", 20),
    ("LAB-PWK-005", "Kompas Survey", "PWK", 15),

    # ================= INDUSTRI =================
    ("LAB-TI-001", "Stopwatch Industri", "Industri", 20),
    ("LAB-TI-002", "Work Measurement Board", "Industri", 5),
    ("LAB-TI-003", "Ergonomic Chair", "Industri", 12),
    ("LAB-TI-004", "Simulation Kit Lean", "Industri", 6),
    ("LAB-TI-005", "Layout Planning Board", "Industri", 4),

    # ================= IT =================
    ("LAB-IF-001", "PC Praktikum", "IT", 30),
    ("LAB-IF-002", "Server Rack Mini", "IT", 4),
    ("LAB-IF-003", "Router Mikrotik", "IT", 12),
    ("LAB-IF-004", "Switch Managed", "IT", 10),
    ("LAB-IF-005", "Access Point", "IT", 15),
    ("LAB-IF-006", "Network Cable Tester", "IT", 10),

    # ================= MESIN =================
    ("LAB-TM-001", "Mesin Bubut", "Mesin", 4),
    ("LAB-TM-002", "Mesin Frais", "Mesin", 3),
    ("LAB-TM-003", "Vernier Caliper", "Mesin", 20),
    ("LAB-TM-004", "Micrometer Screw Gauge", "Mesin", 18),
    ("LAB-TM-005", "Surface Roughness Tester", "Mesin", 4),

    # ================= ARSITEKTUR =================
    ("LAB-AR-001", "Drawing Table", "Arsitektur", 15),
    ("LAB-AR-002", "Architect Scale Ruler", "Arsitektur", 30),
    ("LAB-AR-003", "3D Printer", "Arsitektur", 3),
    ("LAB-AR-004", "Cutting Mat", "Arsitektur", 20),
    ("LAB-AR-005", "Laser Cutter", "Arsitektur", 2),

    # ================= SISTEM INFORMASI =================
    ("LAB-SI-001", "PC SIMLAB", "Sistem Informasi", 25),
    ("LAB-SI-002", "Database Server", "Sistem Informasi", 4),
    ("LAB-SI-003", "Barcode Scanner", "Sistem Informasi", 10),
    ("LAB-SI-004", "RFID Reader", "Sistem Informasi", 6),
    ("LAB-SI-005", "UPS Server", "Sistem Informasi", 8),
]

# ======================
# SETUP FILE
# ======================
def setup_files():
    if not os.path.exists(FILE_INVENTARIS):
        with open(FILE_INVENTARIS, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["kode", "nama", "jurusan", "total", "tersedia"])
            for k, n, j, t in inventaris_awal:
                w.writerow([k, n, j, t, t])

    if not os.path.exists(FILE_PEMINJAMAN):
        with open(FILE_PEMINJAMAN, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow([
                "no_pinjam", "nama_peminjam", "nim",
                "kode_alat", "nama_alat", "qty",
                "tgl_pinjam", "jatuh_tempo",
                "tgl_kembali", "hari_telat",
                "total_denda", "petugas", "status"
            ])

# ======================
# LOGIN
# ======================
def login_petugas():
    print("=== LOGIN PETUGAS LAB ===")
    while True:
        nama = input("Nama Petugas: ").strip()
        if nama:
            return nama

# ======================
# UTIL
# ======================
def generate_no_pinjam():
    today = datetime.date.today().strftime("%Y%m%d")
    count = 1
    with open(FILE_PEMINJAMAN, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["no_pinjam"].startswith(f"INV-{today}"):
                count += 1
    return f"INV-{today}-{count:04d}"

def baca_inventaris():
    with open(FILE_INVENTARIS, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def simpan_inventaris(data):
    with open(FILE_INVENTARIS, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["kode", "nama", "jurusan", "total", "tersedia"])
        for d in data:
            w.writerow(d.values())

# ======================
# MENU
# ======================
def tampil_menu():
    print("\n" + "="*LEBAR)
    print(NAMA_SISTEM.center(LEBAR))
    print("="*LEBAR)
    print("1. Lihat Inventaris")
    print("2. Peminjaman Alat")
    print("3. Pengembalian Alat")
    print("4. Laporan Denda")
    print("0. Keluar")

# ======================
# FITUR
# ======================
def lihat_inventaris():
    data = baca_inventaris()
    print("\nDAFTAR INVENTARIS LAB FT\n")
    for i, d in enumerate(data, 1):
        print(f"{i:02}. [{d['jurusan']:<15}] {d['nama']:<35} | Tersedia: {d['tersedia']}")

def peminjaman(petugas):
    data = baca_inventaris()
    lihat_inventaris()

    idx = int(input("\nPilih alat (nomor): ")) - 1
    alat = data[idx]

    if int(alat["tersedia"]) == 0:
        print("❌ Stok habis")
        return

    nama = input("Nama Peminjam: ")
    nim = input("NIM/NIP: ")
    qty = int(input("Jumlah pinjam: "))
    hari = int(input("Lama pinjam (hari): "))

    if qty > int(alat["tersedia"]):
        print("❌ Stok tidak cukup")
        return

    no = generate_no_pinjam()
    tgl_pinjam = datetime.date.today()
    jatuh = tgl_pinjam + datetime.timedelta(days=hari)

    alat["tersedia"] = str(int(alat["tersedia"]) - qty)
    simpan_inventaris(data)

    with open(FILE_PEMINJAMAN, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            no, nama, nim,
            alat["kode"], alat["nama"], qty,
            tgl_pinjam, jatuh,
            "", 0, 0, petugas, "DIPINJAM"
        ])

    print(f"✅ Peminjaman berhasil | Nomor: {no}")

def pengembalian(petugas):
    no = input("Nomor Peminjaman: ")

    with open(FILE_PEMINJAMAN, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    target = next((r for r in rows if r["no_pinjam"] == no and r["status"] == "DIPINJAM"), None)
    if not target:
        print("❌ Data tidak ditemukan")
        return

    kembali = datetime.date.today()
    jatuh = datetime.date.fromisoformat(target["jatuh_tempo"])
    telat = max((kembali - jatuh).days, 0)
    denda = telat * int(target["qty"]) * DENDA_PER_HARI

    data = baca_inventaris()
    for d in data:
        if d["kode"] == target["kode_alat"]:
            d["tersedia"] = str(int(d["tersedia"]) + int(target["qty"]))
    simpan_inventaris(data)

    for r in rows:
        if r["no_pinjam"] == no:
            r.update({
                "tgl_kembali": str(kembali),
                "hari_telat": str(telat),
                "total_denda": str(denda),
                "petugas": petugas,
                "status": "SELESAI"
            })

    with open(FILE_PEMINJAMAN, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(rows[0].keys())
        for r in rows:
            w.writerow(r.values())

    garis = "="*LEBAR
    bukti = [
        NAMA_SISTEM.center(LEBAR),
        garis,
        f"No Peminjaman : {no}",
        f"Peminjam      : {target['nama_peminjam']} ({target['nim']})",
        f"Alat          : {target['nama_alat']}",
        f"Jumlah        : {target['qty']}",
        f"Tgl Pinjam    : {target['tgl_pinjam']}",
        f"Jatuh Tempo   : {target['jatuh_tempo']}",
        f"Tgl Kembali   : {kembali}",
        f"Hari Telat    : {telat}",
        f"TOTAL DENDA   : Rp{denda:,}",
        garis,
        f"Petugas       : {petugas}",
        "STATUS        : SELESAI"
    ]

    print("\n" + "\n".join(bukti) + "\n")
    with open(f"bukti_{no}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(bukti))

def laporan_denda():
    total = 0
    with open(FILE_PEMINJAMAN, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            total += int(r["total_denda"])
    print(f"\nTOTAL DENDA TERKUMPUL: Rp{total:,}")

# ======================
# MAIN
# ======================
setup_files()
petugas = login_petugas()

while True:
    tampil_menu()
    p = input("Pilih menu: ")

    if p == "1":
        lihat_inventaris()
    elif p == "2":
        peminjaman(petugas)
    elif p == "3":
        pengembalian(petugas)
    elif p == "4":
        laporan_denda()
    elif p == "0":
        print("Sistem ditutup.")
        break
    else:
        print("❌ Menu tidak valid")

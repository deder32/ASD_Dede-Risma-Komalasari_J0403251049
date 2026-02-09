# ====================================
# Load Data
# =====================================
nama_file = "stok_barang.txt"

def baca_data_stok_barang(nama_file):
    data_sementara = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                parts = baris.split(",")
                if len(parts) != 3:
                    continue
                kodebarang, namabarang, stok_str = parts
                try:
                    data_sementara[kodebarang] = {
                        "namabarang": namabarang,
                        "stok": int(stok_str)
                    }
                except ValueError:
                    continue
        return data_sementara
    except FileNotFoundError:
        # Jika file belum ada, buat file kosong
        open(nama_file, "w").close()
        return {}

# ===========================================
# Menu 1 : Menampilkan semua barang 
# ===========================================

def tampilkan_stok_barang(data_input):
    if not data_input:
        print("\n[!] Data stok barang kosong")
        return
    print("\n============== STOK BARANG =============")
    print(f"{'Kode Barang':<12} | {'Nama Barang':<15} | {'Stok' :<5}")
    print("=" * 40)

    for kode in sorted(data_input.keys()):
        nama = data_input[kode]["namabarang"]
        stok = data_input[kode]["stok"] # Perbaikan: Gunakan data_input, bukan data_dict global
        print(f"{kode:<12} | {nama:<15} | {stok:>5}")

# ===============================================
# Menu 2: Cari data berdasarkan kode barang
# ===============================================

def cari_stokbarang(data_input):
    cari_kodebarang = input("Masukkan Kode barang yang ingin dicari: ").strip()
    if cari_kodebarang in data_input:
        nama = data_input[cari_kodebarang]["namabarang"]
        stok = data_input[cari_kodebarang]["stok"]

        print("\n======== Data stok barang ditemukan =======")
        print(f"Kode Barang = {cari_kodebarang}")
        print(f"Nama Barang = {nama}")
        print(f"Stok        = {stok}")
    else:
        print("\n[!] Data tidak ditemukan.")

# ==========================================
# Menu 3 : Tambah barang baru
# ==========================================

def tambah_barang_baru(data_input):
    print("\n========= Tambah Data ========")
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in data_input:
        print("Gagal! kode barang sudah ada dalam sistem")
        return
    
    nama = input("Masukkan nama barang baru: ").strip()
    try:
        stok = int(input("Masukkan stok barang baru: "))
        data_input[kode] = {
            "namabarang": nama,
            "stok": stok
        }
        print(f"Berhasil: Barang '{nama}' telah ditambahkan.")
    except ValueError:
        print("Gagal: Stok harus berupa angka.")

# =====================================================
# Menu 4: Update Stok barang
# =====================================================

def update_stok_barang(data_input):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in data_input:
        print("[!] Kode barang tidak ditemukan.")
        return
    
    try:
        stok_baru = int(input(f"Masukkan stok baru untuk {data_input[kode]['namabarang']}: ").strip())
        stok_lama = data_input[kode]["stok"] # Perbaikan: Gunakan key "stok"
        data_input[kode]["stok"] = stok_baru # Perbaikan: Gunakan key "stok"
        print(f"Berhasil! Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}.")
    except ValueError:
        print("Gagal! Nilai harus angka.")

# ===========================================
# Menu 5: Simpan File
# ===========================================

def simpan_data_ke_file(nama_file, data_input):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            for kode in sorted(data_input.keys()):
                nama = data_input[kode]["namabarang"]
                stok = data_input[kode]["stok"] # Perbaikan: Gunakan key "stok"
                file.write(f"{kode},{nama},{stok}\n")
        print(f"Data berhasil disimpan ke {nama_file}")
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")

# ===============================================
# Menu Utama (Main Program)
# ===============================================

def main():
    # Load data otomatis saat program dimulai
    buka_data = baca_data_stok_barang(nama_file)

    while True:
        print("\n=== MENU STOK BARANG ===")
        print("1. Tampilkan Data Stok Barang")
        print("2. Cari Data Berdasarkan Kode Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Simpan ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_stok_barang(buka_data)

        elif pilihan == "2":
            cari_stokbarang(buka_data)

        elif pilihan == "3":
            tambah_barang_baru(buka_data)

        elif pilihan == "4":
            # Perbaikan: Fungsi update tadi kamu panggil dengan 2 parameter padahal definisinya 1
            update_stok_barang(buka_data)
    
        elif pilihan == "5":
            simpan_data_ke_file(nama_file, buka_data)

        elif pilihan == "0":
            # Menawarkan simpan sebelum keluar
            tanya = input("Simpan perubahan sebelum keluar? (y/n): ").lower()
            if tanya == 'y':
                simpan_data_ke_file(nama_file, buka_data)
            print("Program Selesai.")
            break

        else:
            print("[!] Pilihan tidak valid.")

if __name__ == "__main__":
    main()
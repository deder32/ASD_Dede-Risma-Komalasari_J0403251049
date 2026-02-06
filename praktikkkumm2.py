import os

# ================================================
# Variabel Global
# ================================================
nama_file = "data_mahasiswa.txt"

# ================================================
# Latihan 1: Membuat Fungsi Load Data
# ================================================
def baca_data(nama_file):
    data_dict = {} 
    
    # Cek apakah file ada agar tidak error
    if not os.path.exists(nama_file):
        # Buat file kosong jika belum ada
        with open(nama_file, "w", encoding="utf-8") as f:
            pass
        return data_dict

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if baris: # Pastikan baris tidak kosong
                parts = baris.split(",")
                if len(parts) == 3: # Pastikan format nim,nama,nilai pas
                    nim, nama, nilai = parts
                    # .strip() untuk membersihkan spasi di sekitar nama/nim
                    data_dict[nim.strip()] = {"nama": nama.strip(), "nilai": int(nilai.strip())}
    
    # PERBAIKAN: Return harus sejajar dengan with, bukan di dalam for loop
    return data_dict

# ================================================
# Latihan 2: Menampilkan Data
# ================================================
def tampilkan_data(data_dict):
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' : <10} | {'Nama': <12} | {'Nilai': >5}")
    print("-" * 35)

    if not data_dict:
        print("Belum ada data.")
    else:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            # PERBAIKAN: Kolom ketiga harus variable 'nilai', bukan 'nama'
            print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

# ================================================
# Latihan 3: Mencari Data
# ================================================
def cari_data(data_dict):
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()
     
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else: 
        print("Data tidak ditemukan, pastikan NIM yang anda input sudah benar.")

# ================================================
# Latihan 4: Update Data (Perbaikan Logic)
# ================================================
def ubah_data(data_dict):
    nim = input("Masukkan NIM Mahasiswa yang ingin diubah datanya: ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan.")
        return # Stop fungsi

    # PERBAIKAN: Input string dulu, baru convert int
    try:
        input_nilai = input("Masukkan nilai baru (0-100): ").strip()
        nilai_baru = int(input_nilai)
    except ValueError:
        print("Error: Nilai harus berupa angka. Update dibatalkan.")
        return # Stop fungsi

    if nilai_baru < 0 or nilai_baru > 100:
        print("Error: Nilai harus antara 0 sampai 100. Update dibatalkan.")
        return # Stop fungsi

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

# ================================================
# Latihan 5: Menyimpan Data (Perbaikan Fatal)
# ================================================
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"] # PERBAIKAN: Key harus "nama" bukan "nim"
            nilai = data_dict[nim]["nilai"]
            # PERBAIKAN: Tambahkan \n agar ganti baris
            file.write(f"{nim},{nama},{nilai}\n") 

    # HAPUS baris: simpan_data(...) di sini karena akan menyebabkan Loop Tak Terbatas (RecursionError)
    print("\nData Berhasil Disimpan ke File:", nama_file)

# ================================================
# Latihan 6: Menu Interaktif (MAIN)
# ================================================
def main():
    # Load data sekali saja di awal
    data_mahasiswa = baca_data(nama_file) 
    print(f"Data berhasil dimuat: {len(data_mahasiswa)} data.")

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan data Mahasiswa")
        print("2. Cari data berdasarkan NIM")
        print("3. Ubah data mahasiswa")
        print("4. Simpan data") # Pisahkan simpan dan keluar agar aman
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
        elif pilihan == "2":
            cari_data(data_mahasiswa)
        elif pilihan == "3":
            ubah_data(data_mahasiswa)
        elif pilihan == "4":
            simpan_data(nama_file, data_mahasiswa)
        elif pilihan == "0":
            # Opsi: Simpan otomatis saat keluar
            konfirmasi = input("Simpan perubahan sebelum keluar? (y/n): ").lower()
            if konfirmasi == 'y':
                simpan_data(nama_file, data_mahasiswa)
            print("Program Selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# ================================================
# EKSEKUSI PROGRAM
# ================================================
if __name__ == "__main__":
    main()
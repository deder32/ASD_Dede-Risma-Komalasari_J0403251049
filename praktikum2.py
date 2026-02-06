# ================================================
# Praktikum 2: Konsep ADT dan file Handling(Study Kasus)
# Latihan 1: Membuat Fungsi Load Data
# ================================================

# Variabel Menyimpan Data
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                nim, nama, nilai = baris.split(",")
                data_dict[nim] = {"nama": nama, "nilai": int(nilai)}
        return data_dict
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan. Membuat file baru.")
        return {}

buka_data = baca_data(nama_file)
print("Jumlah data terbaca:", len(buka_data))

# ================================================
# Praktikum 2: Konsep ADT dan file Handling(Studi Kasus)
# Latihan 2: Membuat fungsi menampilkan data
# ================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' : <10} | {'Nama': <12} | {'Nilai': >5}")
    '''
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' : <10 artinya nim rata kiri dengan lebar 10 karakter}
    {'Nama' : <12 artinya nim rata kiri dengan lebar 12 karakter}
    {'Nilai' : >5 artinya nim rata kanan dengan lebar 5 karakter}
    '''
    print("-" *32) #Membuat garis

    #Menampilkan isi data
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

# ================================================
# Praktikum 2: Konsep ADT dan file Handling(Studi Kasus)
# Latihan 3: Membuat fungsi mencari data
# ================================================

#Membuat fungsi pencarian data
def cari_data(data_dict):
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()
     
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("=== Data Mahasiswa Ditemukan ===")
        print(f"NIM        : {nim_cari}")
        print(f"Nama       : {nama}")
        print(f"Nilai      : {nilai}")
    else: 
        print("Data tidak ditemukan, pastikan NIM yang anda input sudah benar")

# ================================================
# Praktikum 2: Konsep ADT dan file Handling(Studi Kasus)
# Latihan 4: Membuat fungsi update data
# ================================================

#Membuat fungsi update data
def ubah_data(data_dict):
    #Awali dgn mencari nim/data mahasiswa yang ingin di update
    nim = input("Masukkan NIM Mahasiswa yang ingin diubah datanya: ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai dari 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    return data_dict

# ================================================
# Praktikum 2: Konsep ADT dan file Handling(Studi Kasus)
# Latihan 5
# ================================================

#Membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("\nData Berhasil Disimpan ke File:", nama_file)

# ================================================
# Praktikum 2: Konsep ADT dan file Handling(Studi Kasus)
# Latihan 6: Membuat Menu Interaktif
# ================================================

def main():
    #load data otomatis saat program dimulai
    data_mahasiswa = baca_data(nama_file) #fs.1 

    while True:
        print("\n=== DATA MAHASISWA ===")
        print("1. Tampilkan data Mahasiswa")
        print("2. Cari data berdasarkan NIM")
        print("3. Ubah data mahasiswa")
        print("4. Simpan data")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
        elif pilihan == "2":
            cari_data(data_mahasiswa)
        elif pilihan == "3":
            data_mahasiswa = ubah_data(data_mahasiswa)
        elif pilihan == "4":
            simpan_data(nama_file, data_mahasiswa)
        elif pilihan == "0":
            konfirmasi = input("Simpan data sebelum keluar? (y/n): ").strip().lower()
            if konfirmasi == 'y':
                simpan_data(nama_file, data_mahasiswa)
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 0-4")

if __name__ == "__main__":
    main()
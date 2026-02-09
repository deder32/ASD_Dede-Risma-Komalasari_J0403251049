#=======================================================
# Praktikum 2: Konsep ADT dan File Handing(STUDI KASUS)
# Latihan 1: Membuat Fungsi Load Data dari File
#=======================================================

#variabel menyimpan data file
nama_file = "data.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim]= {"nama": nama, "nilai": int(nilai)}
        return data_dict 
    
buka_data = baca_data(nama_file) 
print ("jumlah data terbaca", len(buka_data))


#=======================================================
# Praktikum 2: Konsep ADT dan File Handing(STUDI KASUS)
# Latihan 2: Membuat Fungsi Menampilkan Data
#=======================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' : <10} | {'Nama': <12}  | {'Nilai' :>5}")
    '''
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM': <10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nama': <12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai' :>5} artinya nilai rata kanan dengan lebar kolom 5 karakter
    '''
    print("-"*32) #Membuat garis

    #Menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):<5}")

tampilkan_data(buka_data) #Memanggil fungsi untuk menampilkan data


#=======================================================
# Praktikum 2: Konsep ADT dan File Handing(STUDI KASUS)
# Latihan 3: Membuat Fungsi Mencari data
#=======================================================

def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("masukkan NIM mahasiswa yang ingin dicari: ".strip())

    if nim_cari in data_dict:
        nama= data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("==== Data Mahasiswa Ditemukan ====")
        print(f"NIM  : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai :{nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukan benar")

    #memanggil fungsi cari data
    cari_data(buka_data)
    

#=======================================================
# Praktikum 2: Konsep ADT dan File Handing(STUDI KASUS)
# Latihan 4: Membuat Fungsi Update Data
#=======================================================
#membuat fungsi update data
def ubah_data(data_dict):
    #Awali dgn mencari nim/data mahasiswa yang ingin di update
    nim = input("Masukkan NIM Mahasiswa yang ingin diubah datanya")

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai dari 0-100: ")).strip()
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return 
    
    if nilai_baru < 0 or nilai_baru >100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")
        return
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi nilai baru")
    ubah_data(buka_data)

#=======================================================
# Praktikum 2: Konsep ADT dan File Handing(STUDI KASUS)
# Latihan 5: Membuat Fungsi Menyimpan Data pada File
#=======================================================

#membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nim"]
            nilai = data_dict[nilai]["nilai"]
            file.write(f"{nim}, {nama,}, {nilai}\n")

        simpan_data(nama_file, buka_data)
        print("\nData Berhasil Disimpan Ke File :", nama_file)

#=======================================================
# Praktikum 2: Konsep ADT dan File Handing(STUDI KASUS)
# Latihan 6: Membuat Menu Interaktif
#=======================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #memanggil fs 2 menampilkan data

        elif pilihan == "2":            #memanggil fs.3 mencari data
            cari_data(buka_data)

        elif pilihan == "3":             #memanggil fs.4 mengubah data
            ubah_data(buka_data)

        elif pilihan == "4" :                    #memanggil fs.5 menyimpan data ke file
            simpan_data(nama_file, buka_data)
    
        elif pilihan == "0":
            print("Program Selesai.")
            break

        else:
            print("kesalahan")

if __name__ == "__main__":
    main()
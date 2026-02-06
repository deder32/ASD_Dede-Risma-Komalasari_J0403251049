#==================================
#Praktikum 1 : Konsep ADT dan file handing
#Latihan dasar 1 : Membaca seluruh isi file data
#=====================================

print("==Membuka File dalam satu string===")
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file :
    isi_file = file.read()
print(isi_file)

print("Tipe Data :", type(isi_file))

print("===Membuka file perbaris===")
jumlah_baris = 0 #inisialisasi variabel untuk menghitung
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file :
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("baris ke", jumlah_baris)
        print("isinya :", baris)

#Parsing baris menjadi satuan dan menampilkannya dalam bentuk kolom-kolom data
jumlah_baris = 0 #inisialisasi variabel untuk menghitung
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file :
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan disimpan dalam varibel
        print("NIM: ", nim, "nama", "| Nama: ", nama, "| Nilai ", nilai) #untuk menampilkan kolom


data_list=[]
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file :
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai= baris.split(",")
        data_list.append([nim,nama,int(nilai)])
print("===Menampilkan list===")
print(data_list)
print("Contoh record ke 1", data_list[0])
print("Contoh record ke-2", data_list[1])
print("Jumlah Record", len(data_list))


#============================================================
#Latihan dasar 3: Membaca dan mnyimpannya ke struktur data list
#=============================================================
data_dict = {}
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file :
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai=baris.split(",")
        data_dict[nim] = {
                "nama" : nama,
                "nilai" : int(nilai)
        }
print("=== Menampilkan data dictionary")
print(data_dict)
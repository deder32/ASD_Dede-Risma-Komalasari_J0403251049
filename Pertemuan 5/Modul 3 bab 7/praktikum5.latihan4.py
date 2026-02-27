# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# Nama: Dede Risma Komalasari
# NIM: J0403251049
# ========================================================== 
 
def kombinasi(n, hasil=""): 
 
    # 1. Base Case
    # Jika panjang string 'hasil' sudah sama dengan 'n', 
    # cetak hasilnya dan berhenti (kembali ke tumpukan sebelumnya).
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    # 2. Recursive Call
    # Setiap langkah akan bercabang menjadi dua pilihan:
    
    # Cabang kiri: Menambahkan huruf "A" ke kombinasi saat ini
    kombinasi(n, hasil + "A") 
    
    # Cabang kanan: Menambahkan huruf "B" ke kombinasi saat ini
    # Baris ini baru akan jalan setelah semua cabang "A" di atas selesai.
    kombinasi(n, hasil + "B") 
 
# Menjalankan fungsi untuk kombinasi 2 huruf
kombinasi(2)

# Jumlah kombinasi dihasilkan dengan cara bekerja seperti pohon 
# keputusan yang setiap tingkatnya terdiri dari:
# Mulai: Kosong ("")
# Tingkat 1: Bercabang menjadi A dan B.
# Tingkat 2: * Dari A bercabang lagi menjadi AA dan AB.
#        Dari B bercabang lagi menjadi BA dan BB.
# ========================================================== 
# Latihan 2: Tracing Rekursi 
# Nama: Dede Risma Komalasari
# NIM: J0403251049
# ========================================================== 
def countdown(n): 
    # 1. Cek apakah angka sudah mencapai batas akhir (0)
    if n == 0: 
        print("Selesai") 
        return # Mengakhiri fungsi dan mulai kembali ke pemanggil sebelumnya
 
    # 2. Menampilkan angka saat fungsi baru dipanggil
    print("Masuk:", n) 
 
    # 3. PROSES REKURSI yakni Memanggil diri sendiri dengan n yang dikurangi 1
    # Baris setelah ini (print Keluar) akan ditangguhkan/antri di memori
    countdown(n - 1) 
 
    # 4. Menampilkan angka setelah fungsi di bawahnya selesai (return)
    # Ini mengambil nilai n yang tersimpan di tumpukan memori (Stack)
    print("Keluar:", n) 
 
# Titik awal program dijalankan
countdown(3)

# Alasan mengapa output 'keluar' muncul terbalik
# 1. Setiap kali program memproses countdown(n), baris 
# print("Keluar") tidak langsung dijalankan. Baris itu 
# "dititipkan" di memori karena program harus terjun ke 
# n-1 terlebih dahulu.
# 2. Perintah Keluar: 3 ditaruh paling bawah, lalu Keluar: 2 
# di atasnya, dan Keluar: 1 di paling atas.
# 3. Setelah mencapai n=0 (Selesai), program mulai mengambil titipan tadi. 
# Karena prinsipnya adalah mengambil dari yang paling atas, maka 
# Keluar: 1 diambil duluan, baru Keluar: 2, dan terakhir Keluar: 3.
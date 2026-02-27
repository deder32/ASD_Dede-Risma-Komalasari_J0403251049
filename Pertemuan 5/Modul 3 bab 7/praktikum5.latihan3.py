# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# Nama: Dede Risma Komalasari
# NIM: J0403251049
# ========================================================== 
 
def cari_maks(data, index=0): 
 
    # 1. Kondisi Berhenti
    # Jika index sudah sampai di elemen terakhir, kembalikan nilai tersebut.
    # Di sinilah program berhenti dan mulai membawa angka untuk dibanding.
    if index == len(data) - 1: 
        return data[index] 
 
    # 2. RECURSIVE CALL
    # Program terus melompat ke index berikutnya (index + 1) sampai ke ujung.
    # Variabel 'maks_sisa' akan menyimpan pemenang dari elemen-elemen di depannya.
    maks_sisa = cari_maks(data, index + 1) 
 
    # 3. Alur balik
    # Setelah kembali dari rekursi, kita bandingkan angka saat ini dengan 
    # angka terbesar yang ditemukan dari sisa data di depannya.
    if data[index] > maks_sisa: 
        return data[index] # Angka saat ini lebih besar, dia jadi pemenang baru
    else: 
        return maks_sisa   # Angka di depannya lebih besar, pemenang tetap sama
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))
# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# Nama: Dede Risma Komalasari
# NIM: J0403251049
# ========================================================== 

def pangkat(a, n): 
    # 1. Base Case
    # Jika pangkat (n) sudah nol, program berhenti  
    # dan mulai mengirim balik angka 1 ke atas.
    if n == 0: 
        return 1 
    
    # 2. Proses Rekursi
    # Program belum bisa mengalikan 'a' sekarang karena harus tahu 
    # hasil dari 'pangkat(a, n - 1)' terlebih dahulu.
    # Ini akan menumpuk operasi perkalian di memori (Stack).
    return a * pangkat(a, n - 1) 

# 3. Memanggil 2 pangkat 4.
print(pangkat(2, 4))  # Output: 16

# Alur program serta base case dan recursive call
# 1. Base Case
# Sebagai batas akhir. Tanpa fungsi ini, program akan terus mengurangi 
# n sampai angka negatif dan menyebabkan error (stack overflow).
# 2. Recursive Call
# Untuk memecah masalah besar menjadi lebih kecil.
# 3. Alur program (Tracing)
# - Program terus memanggil dirinya sendiri sampai menyentuh base case:
# - 1. Pangkat 2, 4 yaitu menunda 2 x sampai selesai (memanggil pangkat 2, 3)
# - 2. Pangkat 2, 3 yaitu menunda 2 x sampai selesai (memanggil pangkat 2, 2)
# - 3. Pangkat 2, 2 yaitu menunda 2 x sampai selesai (memanggil pangkat 2, 1)
# - 4. Pangkat 2, 1 yaitu menunda 2 x sampai selesai (memanggil pangkat 2, 0)
# - 5. Pangkat(2, 0) yaitu berhenti dan mengembalikan nilai 1.
# 4. Menyelesaikan (menghitung balik)
# Setelah mendapat angka 1, program "naik kembali" untuk menyelesaikan perkalian yang tadi ditunda
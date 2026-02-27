# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# Nama: Dede Risma Komalasari
# NIM: J0403251049 
# ========================================================== 
def hitung(n): 
# Base case 
    if n == 0: 
        print("Selesai") 
        return 
    print("Masuk:", n)  # fase stacking    
    hitung(n - 1)       # pemanggilan rekursif 
    print("Keluar:", n) # fase unwinding 
hitung(3)
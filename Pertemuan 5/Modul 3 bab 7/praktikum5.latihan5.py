# ========================================================== 
# Studi Kasus: Generator PIN (Tanpa Angka Berulang)
# Nama: Dede Risma Komalasari
# NIM: J0403251049
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    # 1. BASE CASE
    # Program berhenti jika panjang PIN sudah sesuai target.
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
 
    # 2. Looping pemilihan angka
    for angka in ["0", "1", "2"]: 
        
        # 3. CEK VALIDASI 
        # Sebelum masuk ke rekursi berikutnya, program mengecek
        # "Apakah angka ini sudah ada di dalam rangkaian 'hasil'?"
        if angka not in hasil: 
            
            # Jika angka belum ada, maka aman untuk ditambahkan
            # dan lanjut ke tingkatan berikutnya (rekursi).
            buat_pin(panjang, hasil + angka) 
            
        # Jika angka SUDAH ada, loop akan mengabaikan baris rekursi 
        # dan langsung pindah ke angka berikutnya.
 
# Membuat PIN 3 digit dari angka 0, 1, 2
buat_pin(3)
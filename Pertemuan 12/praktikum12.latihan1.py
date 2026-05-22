# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Latihan 1)

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D secara manual
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis Latihan 1:
# ==========================================================
# 1. Total bobot jalur A -> B -> D adalah 4 + 5 = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 + 1 = 3.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D karena memiliki total bobot terkecil (3).
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit karena algoritma shortest path 
#    berfokus pada "biaya minimum" (total bobot terkecil), bukan jumlah langkah perjalanan. Jalur dengan edge 
#    lebih banyak bisa saja memiliki akumulasi bobot yang jauh lebih kecil daripada jalur langsung berbobot besar.
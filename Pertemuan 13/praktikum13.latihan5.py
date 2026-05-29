# Nama : Dede Risma Komalasari
# NIM  : J0403251049
# Kelas: TPL A3
# Praktikum 13 - Graph III: Spanning Tree (Latihan 5 Kasus 1)

# 1. Representasi Weighted Graph menggunakan daftar edge global
# Kasus 1: Jaringan Jalan Antar Kota
# Bobot merepresentasikan jarak/biaya antar kota
jaringan_jalan = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. Implementasi Algoritma Kruskal
# Langkah awal Kruskal: Urutkan semua edge berdasarkan bobot terkecil (Greedy)
jaringan_jalan.sort()

mst_jalan = []
total_jarak_minimum = 0
connected_cities = set()

# Iterasi dan seleksi edge
for weight, u, v in jaringan_jalan:
    # Memilih edge jika salah satu atau kedua kota belum terhubung sepenuhnya
    # (Pencegahan cycle sederhana untuk struktur data set)
    if u not in connected_cities or v not in connected_cities:
        mst_jalan.append((u, v, weight))
        total_jarak_minimum += weight
        connected_cities.add(u)
        connected_cities.add(v)

# 3 & 4. Output Jalur MST dan Total Bobot Minimum
print("--- Hasil Optimasi MST Jaringan Jalan Antar Kota ---")
print("Jalur jalan yang terpilih untuk dibangun:")
for edge in mst_jalan:
    print(f"Rute {edge[0]} - {edge[1]} dengan Jarak/Bobot: {edge[2]}")

print(f"\nTotal Jarak Minimum Jaringan = {total_jarak_minimum}")


# ==============================================================================
# JAWABAN PERTANYAAN ANALISIS
# ==============================================================================
# # Jawab Analisis:
# # 1. Kasus apa yang dipilih?
# #    Jawab: Kasus 1. Jaringan Jalan Antar Kota (Bogor, Depok, Jakarta, Bandung).
# #
# # 2. Algoritma apa yang digunakan?
# #    Jawab: Algoritma Kruskal (dengan pengurutan edge berbasis bobot terkecil).
# #
# # 3. Edge mana saja yang dipilih dalam MST?
# #    Jawab: Edge yang terpilih adalah:
# #           - Bogor - Depok (Bobot: 2)
# #           - Depok - Jakarta (Bobot: 3)
# #           - Depok - Bandung (Bobot: 4)
# #
# # 4. Berapa total bobot MST?
# #    Jawab: Total bobot (jarak minimum) MST yang dihasilkan adalah 9.
# #
# # 5. Mengapa edge tertentu tidak dipilih?
# #    Jawab: 
# #    - Edge 'Bogor - Jakarta' (Bobot: 5) tidak dipilih karena Bogor dan Jakarta 
# #      sudah terhubung secara tidak langsung melalui Depok (Bogor-Depok-Jakarta). 
# #      Jika dibangun, jalan tersebut akan membentuk siklus (loop) yang mubazir.
# #    - Edge 'Jakarta - Bandung' (Bobot: 6) tidak dipilih karena Bandung sudah 
# #      berhasil terhubung ke jaringan utama via Depok dengan biaya yang lebih murah (4). 
# #      Mengambil jalan berbobot 6 hanya akan memboroskan total jarak pembangunan.
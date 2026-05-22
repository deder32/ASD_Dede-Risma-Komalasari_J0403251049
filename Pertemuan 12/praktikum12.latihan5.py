# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Latihan 5)

import heapq

# 1. Representasi graph berbobot menggunakan dictionary bersarang (nested dictionary)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra_kota(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# 3. Input node awal / Penentuan node awal di dalam program
node_awal = 'Bogor'
hasil = dijkstra_kota(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node sesuai format yang diharapkan
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis Latihan 5:
# ==========================================================
# 1. Node awal yang digunakan dalam program ini adalah 'Bogor'.
# 2. Node yang memiliki jarak paling kecil dari node awal adalah 'Bogor' itu sendiri dengan jarak 0, 
#    diikuti oleh 'Depok' dengan jarak terpendek sebesar 2.
# 3. Node yang memiliki jarak paling besar dari node awal adalah 'Bandung' dengan jarak terpendek sebesar 8.
# 4. Penjelasan cara kerja algoritma Dijkstra pada kasus ini:
#    - Tahap 1: Algoritma mulai dari 'Bogor' (jarak = 0), mengeksplorasi tetangganya, yaitu Jakarta (jarak=5) dan Depok (jarak=2).
#    - Tahap 2: Node dengan jarak terkecil berikutnya dipop, yaitu 'Depok' (jarak=2). Tetangga Depok dieksplorasi, yaitu Jakarta dan Bandung.
#      * Jalur ke Jakarta via Depok menjadi 2 + 2 = 4 (lebih kecil dari jalur langsung Bogor->Jakarta=5, maka jarak Jakarta diperbarui menjadi 4).
#      * Jalur ke Bandung via Depok menjadi 2 + 6 = 8.
#    - Tahap 3: Node berikutnya dipop, yaitu 'Jakarta' (jarak=4). Tetangga Jakarta adalah Bandung dengan bobot 7. Jalur ke Bandung via Jakarta menjadi 4 + 7 = 11 (tidak diperbarui karena 11 > 8).
#    - Tahap 4: Node terakhir 'Bandung' dipop (jarak=8). Semua node selesai diproses dan jarak terpendek final berhasil ditemukan.
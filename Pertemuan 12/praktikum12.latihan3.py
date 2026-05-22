# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Latihan 3)

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis Latihan 3:
# ==========================================================
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B adalah 4 + (-2) = 2.
# 3. Jalur yang menghasilkan jarak lebih kecil menuju B adalah jalur memutar melalui C (A -> C -> B).
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena tidak menggunakan pendekatan greedy. 
#    Algoritma ini melakukan iterasi relaksasi menyeluruh ke semua edge secara berulang sehingga perubahan jarak 
#    akibat bobot negatif akan terus terperbarui hingga optimal.
# 5. Proses relaksasi edge adalah langkah memeriksa apakah jarak ke node tetangga (neighbor) dapat diperkecil/diperbaiki 
#    dengan cara melewati node yang sedang diproses dibandingkan dengan jalur yang telah tercatat sebelumnya.
# 6. Perbedaan utama Bellman-Ford dan Dijkstra: 
#    - Dijkstra: Menggunakan pendekatan Greedy, tidak bisa menangani bobot negatif, tetapi proses eksekusinya jauh lebih cepat.
#    - Bellman-Ford: Menggunakan pendekatan Relaksasi berulang, mampu menangani bobot negatif (serta mendeteksi negative cycle), tetapi proses eksekusinya lebih lambat.
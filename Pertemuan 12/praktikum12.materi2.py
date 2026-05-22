# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Materi Dijkstra)

import heapq

# Implementasi weighted graph dengan bobot positif menggunakan nested dictionary
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Menyimpan jarak minimum sementara ke semua node lalu inisialisasi tak hinggaaa
    distances[start] = 0  # Jarak dari node awal ke diri sendiri adalah 0
    pq = [(0, start)] # Priority queue untuk menyimpan pasangan (jarak, node) agar selalu memproses jarak terkecil
    
    while pq:
        # mengambil node dengan jarak sementara paling kecil (prinsip greedy)
        current_distance, current_node = heapq.heappop(pq)
        
        # Jika ditemukan jarak yang tersimpan lebih kecil dari yang di-pop, lewati proses
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua tetangga dari node yang sedang aktif
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jalur baru dengan bobot yang lebih kecil maka akan melakukan update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Mengeksekusi fungsi dengan node awal 'A'
hasil = dijkstra(graph, 'A')
print("Output Materi Dijkstra:")
print(hasil)
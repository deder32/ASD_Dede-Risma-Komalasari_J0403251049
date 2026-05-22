# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Latihan 4)

import heapq

# Graph lokasi kampus dengan bobot sebagai waktu tempuh (menit)
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
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

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis Latihan 4:
# ==========================================================
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh hanya 2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit (melalui jalur Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7).
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil. Sebagai contoh, dari Kantin ke Aula ada jalur langsung 
#    yang memakan waktu 7 menit. Namun jika melewati Lab (Kantin -> Lab -> Aula), total waktunya menjadi 4 + 1 = 5 menit. 
#    Jadi, jalur memutar bisa memiliki bobot total yang lebih kecil daripada jalur langsung.
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena seluruh bobot yang merepresentasikan waktu tempuh 
#    bernilai positif (tidak ada waktu negatif) dan struktur datanya efisien untuk mencari rute tercepat secara real-time.
# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Latihan 2)

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
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

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis Latihan 2:
# ==========================================================
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3.
# 4. Jarak A ke D lebih kecil melalui C (2 + 1 = 3) dibandingkan melalui B (4 + 5 = 9) karena total akumulasi 
#    bobot pada tepi (edge) jalur C jauh lebih kecil daripada jalur B.
# 5. Fungsi priority_queue adalah untuk menyimpan dan secara otomatis mengurutkan node berdasarkan jarak terkecil 
#    sementara, sehingga algoritma selalu mengambil keputusan terbaik (greedy approach) pada setiap tahapannya secara efisien.
# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena menggunakan prinsip greedy yang mengasumsikan 
#    bahwa node yang sudah selesai diproses/dikunjungi jaraknya bersifat final dan tidak akan berubah lagi. Jika ada bobot 
#    negatif, bisa jadi ada jalur memutar yang lebih murah yang dilewatkan oleh Dijkstra sehingga hasilnya tidak akurat.
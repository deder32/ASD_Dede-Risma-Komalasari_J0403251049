# Nama : Dede Risma Komalasari
# NIM  : J0403251049
# Kelas: TPL A3
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi Graph menggunakan Adjacency List (Dictionary dalam Dictionary)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    # Masukkan semua edge tetangga dari node awal ke dalam min-heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        # Jika node tujuan belum dikunjungi, tandanya aman dari cycle
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan edge dari node baru yang dikunjungi ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan fungsi dari node awal 'A'
mst, total = prim(graph, 'A')

# Menampilkan hasil
print("Minimum Spanning Tree (Prim):")
for edge in mst:
    print(edge)
print("Total bobot =", total)


# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Jawab: Node awal yang digunakan adalah 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Jawab: Edge dari 'A' ke 'C' dengan bobot 2.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Jawab: Prim menentukan edge berikutnya dengan cara melihat seluruh edge yang terhubung ke node-node aktif 
#           (yang sudah dikunjungi/visited), lalu mengekstrak edge dengan bobot paling kecil menggunakan min-heap 
#           yang menuju ke node yang belum pernah dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Jawab: Total bobot yang dihasilkan adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Jawab: Kruskal berfokus pada EDGE secara global dengan mengurutkan seluruh edge di graph terlebih dahulu tanpa 
#           melihat node asal. Sedangkan Prim berfokus pada NODE, membangun tree secara lokal yang terus membesar 
#           dari satu node acuan secara bertahap.
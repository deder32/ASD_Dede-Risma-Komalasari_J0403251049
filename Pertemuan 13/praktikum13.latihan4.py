# Nama : Dede Risma Komalasari
# NIM  : J0403251049
# Kelas: TPL A3
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# 1. Representasi Weighted Graph menggunakan Adjacency List
graph_gedung = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# 2. Implementasi Algoritma Prim
def prim_studi_kasus(graph, start):
    visited = set([start])
    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_cost = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight
            
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_cost

# Eksekusi Program
mst_kabel, biaya_minimum = prim_studi_kasus(graph_gedung, 'GedungA')

# Output Program
print("--- Jaringan Kabel Internet Antar Gedung ---")
print("Edge (Koneksi) yang dipilih:")
for edge in mst_kabel:
    print(f"{edge[0]} - {edge[1]} dengan biaya: {edge[2]}")
print(f"Total Biaya Minimum = {biaya_minimum}")


# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Jawab: Algoritma Prim (dengan struktur data heapq).
#
# 2. Edge mana saja yang dipilih?
#    Jawab: Edge yang dipilih adalah:
#           - GedungA - GedungC (bobot 2)
#           - GedungC - GedungD (bobot 1)
#           - GedungD - GedungB (bobot 3)
#
# 3. Berapa total biaya minimum?
#    Jawab: Total biaya minimum pemasangan kabel adalah 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Jawab: Karena tujuan kasus ini adalah menghubungkan seluruh gedung agar bisa saling bertukar data internet 
#           dengan kendala biaya pemasangan yang seminimal mungkin dan dipastikan tidak membutuhkan jalur berputar 
#           (cycle) yang memboroskan anggaran kampus.
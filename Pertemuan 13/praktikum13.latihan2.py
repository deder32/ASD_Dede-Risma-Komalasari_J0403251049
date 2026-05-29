# Nama : Dede Risma Komalasari
# NIM  : J0403251049
# Kelas: TPL A3
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil (Strategi greedy Kruskal)
edges.sort()

mst = []
total_weight = 0
connected = set()

# Iterasi secara global pada edge yang sudah terurut
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Menampilkan hasil
print("Minimum Spanning Tree (Kruskal):")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)


# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Jawab: Edge ('C', 'D') dengan bobot 1, karena memiliki bobot terkecil di dalam graph.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Jawab: Karena algoritma Kruskal bekerja menggunakan pendekatan Greedy global, yaitu selalu memprioritaskan 
#           edge dengan biaya terendah demi mencapai total bobot minimum di akhir proses.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Jawab: Total bobot yang dihasilkan adalah 6.
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Jawab: Edge seperti ('A', 'B') dan ('A', 'D') tidak dipilih karena node-node pembentuknya sudah saling 
#           terhubung melalui representasi set `connected`. Jika edge tersebut dipaksa dimasukkan, 
#           maka akan membentuk siklus (cycle) yang melanggar aturan Spanning Tree.
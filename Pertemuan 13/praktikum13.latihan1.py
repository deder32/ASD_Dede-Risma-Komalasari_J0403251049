# Nama : Dede Risma Komalasari
# NIM  : J0403251049
# Kelas: TPL A3
# Praktikum 13 - Graph III: Spanning Tree

# 1. Menampilkan daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Menampilkan contoh spanning tree yang valid (menghubungkan seluruh node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Output Data
print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 3 & 4. Menampilkan jumlah edge awal vs spanning tree
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Jawab: Graph awal dapat memiliki lintasan tertutup (cycle/siklus) dan memiliki edge yang lebih banyak. 
#           Sedangkan Spanning Tree merupakan subgraph yang menghubungkan semua node dari graph asal 
#           tanpa membentuk cycle sama sekali.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Jawab: Karena jika memiliki cycle, koneksi menjadi tidak efisien dan menyebabkan penggunaan 
#           edge berlebih yang dapat meningkatkan total biaya pembangunan jaringan tanpa memberikan 
#           keuntungan fungsional tambahan.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Jawab: Karena spanning tree hanya membutuhkan jumlah minimum edge untuk menghubungkan seluruh node. 
#           Rumus jumlah edge pada spanning tree yang valid selalu tepat: (Jumlah Node - 1).
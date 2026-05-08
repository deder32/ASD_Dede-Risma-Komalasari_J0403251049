# ======================
# Dede Risma Komalasari
# J0403251049
# ======================

def tampilkan_matrix(matrix, nodes=None):
    """Menampilkan adjacency matrix dengan label node."""
    if nodes is None:
        nodes = list(range(len(matrix)))

    print("    " + " ".join(str(node) for node in nodes))
    for node, row in zip(nodes, matrix):
        print(f"{node} : " + " ".join(str(value) for value in row))


def tampilkan_adjacency_list(graph):
    """Menampilkan adjacency list."""
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")


def buat_matrix_tidak_berarah(nodes, edges):
    """Membuat adjacency matrix untuk graph tidak berarah."""
    index = {node: i for i, node in enumerate(nodes)}
    matrix = [[0 for _ in nodes] for _ in nodes]

    for asal, tujuan in edges:
        i = index[asal]
        j = index[tujuan]
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix


def buat_list_tidak_berarah(nodes, edges):
    """Membuat adjacency list untuk graph tidak berarah."""
    graph = {node: [] for node in nodes}

    for asal, tujuan in edges:
        graph[asal].append(tujuan)
        graph[tujuan].append(asal)

    return graph
print("Digit akhir NIM: 9")
print("Studi kasus    : Peta Kota")

nodes_kota = ["Bogor", "Depok", "Jakarta", "Bandung", "Sukabumi"]
edges_kota = [
    ("Bogor", "Depok"),
    ("Bogor", "Sukabumi"),
    ("Depok", "Jakarta"),
    ("Depok", "Sukabumi"),
    ("Jakarta", "Bandung"),
    ("Bandung", "Sukabumi"),
]

graph_kota = buat_list_tidak_berarah(nodes_kota, edges_kota)
matrix_kota = buat_matrix_tidak_berarah(nodes_kota, edges_kota)

print("\nNode / Vertex:")
for kota in nodes_kota:
    print(f"- {kota}")

print("\nEdge / Hubungan antar kota:")
for asal, tujuan in edges_kota:
    print(f"- {asal} terhubung dengan {tujuan}")

print("\nAdjacency List Peta Kota:")
tampilkan_adjacency_list(graph_kota)

print("\nAdjacency Matrix Peta Kota:")
tampilkan_matrix(matrix_kota, nodes_kota)

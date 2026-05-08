# ======================
# Dede Risma Komalasari
# J0403251049
# ======================

def create_graph_matrix(V, edges):
    # Membuat matriks 2D diisi dengan 0 (matriks V x V)
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    # Mengisi matriks berdasarkan list edges
    for u, v in edges:
        mat[u][v] = 1
        mat[v][u] = 1  # Karena graph tidak berarah (undirected)
    return mat

if __name__ == "__main__":
    V = 4
    # 0 terhubung ke 1 dan 2; 2 terhubung ke 1 dan 3
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    
    matrix = create_graph_matrix(V, edges)
    
    # Menampilkan Adjacency Matrix
    print("Adjacency Matrix Representation:")
    for row in matrix:
        print(row)
# ======================
# Dede Risma Komalasari
# J0403251049
# ======================

matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

def convert_matrix_to_list(mat):
    adj_list = {}
    V = len(mat) 
    
    for i in range(V):
        neighbors = []
        for j in range(V):
            if mat[i][j] == 1:
                neighbors.append(j)
        adj_list[i] = neighbors
    return adj_list

if __name__ == "__main__":
    result_list = convert_matrix_to_list(matrix)
    
    print("Hasil Konversi ke Adjacency List:")
    for node, neighbors in result_list.items():
        print(f"{node}: {neighbors}")
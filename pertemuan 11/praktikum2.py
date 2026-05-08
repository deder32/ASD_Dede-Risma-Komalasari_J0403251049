# ======================
# Dede Risma Komalasari
# J0403251049
# ======================

# Representasi Graph menggunakan Dictionary Python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

def display_adjacency_list(adj_list):
    print("Adjacency List Representation:")
    for node, neighbors in adj_list.items():
        print(f"{node}: {' '.join(neighbors)}")

if __name__ == "__main__":
    display_adjacency_list(graph)
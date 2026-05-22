# Nama    : Dede Risma Komalasari
# NIM     : J0403251049
# Kelas   : TPL A2
# Praktikum 12 - Graph II: Shortest Path (Materi Bellman-Ford)

def bellman_ford(graph, start):
    # Inisialisasi awal jarak seluruh node dengan nilai tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak node awal di set 0
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak dari node asal valid dan menghasilkan bobot lebih kecil
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    # update dengan jarak baru yang lebih minim
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Contohhh graph dengan bobot negatif untuk pengujian materi Bellman-Ford
graph_negatif = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

hasil = bellman_ford(graph_negatif, 'A')
print("Output Materi Bellman-Ford:")
print(hasil)
def nearest_neighbor(distance_matrix, start=0):
    n = len(distance_matrix)
    visited = [False] * n
    route = [start]
    visited[start] = True
    total_distance = 0
    current = start

    for _ in range(n - 1):
        nearest = None
        min_dist = float('inf')

        for j in range(n):
            if not visited[j] and distance_matrix[current][j] < min_dist:
                min_dist = distance_matrix[current][j]
                nearest = j

        route.append(nearest)
        visited[nearest] = True
        total_distance += min_dist
        current = nearest

    # kembali ke kota awal
    total_distance += distance_matrix[current][start]
    route.append(start)

    return route, total_distance


# Contoh data (A=0, B=1, C=2, D=3, E=4)
distance_matrix = [
    [0, 10, 15, 20, 25],  # A
    [10, 0, 35, 25, 17],  # B
    [15, 35, 0, 30, 28],  # C
    [20, 25, 30, 0, 22],  # D
    [25, 17, 28, 22, 0]   # E
]

route, total = nearest_neighbor(distance_matrix, start=0)

# Konversi index ke nama kota
cities = ['A', 'B', 'C', 'D', 'E']
route_named = [cities[i] for i in route]

print("Rute:", " -> ".join(route_named))
print("Total jarak:", total)
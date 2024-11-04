import itertools
import time

# Function to calculate the total distance of the tour
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return total_distance

# Exact algorithm using brute force
def tsp_bruteforce(distance_matrix):
    n = len(distance_matrix)
    min_path = None
    min_distance = float('inf')

    # Generate all permutations of cities
    for perm in itertools.permutations(range(n)):
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm
            
    return min_path, min_distance

# Approximation algorithm using Nearest Neighbor
def tsp_nearest_neighbor(distance_matrix, start=0):
    n = len(distance_matrix)
    visited = [False] * n
    tour = [start]
    visited[start] = True

    current_city = start

    for _ in range(n - 1):
        next_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                min_distance = distance_matrix[current_city][city]
                next_city = city
        tour.append(next_city)
        visited[next_city] = True
        current_city = next_city

    return tour, calculate_total_distance(tour, distance_matrix)

def main():
    # Input from user
    n = int(input("Enter the number of cities: "))
    print("Enter the distance matrix (space-separated rows):")
    distance_matrix = []
    
    for i in range(n):
        row = list(map(int, input().strip().split()))
        distance_matrix.append(row)

    # Exact TSP solution
    start_time = time.time()
    exact_tour, exact_distance = tsp_bruteforce(distance_matrix)
    exact_time = time.time() - start_time

    print("\nExact TSP Solution (Brute Force):")
    print(f"Tour: {exact_tour} (Distance: {exact_distance})")
    print(f"Time taken (Exact): {exact_time:.6f} seconds")

    # Approximation TSP solution
    start_time = time.time()
    approx_tour, approx_distance = tsp_nearest_neighbor(distance_matrix)
    approx_time = time.time() - start_time

    print("\nApproximation TSP Solution (Nearest Neighbor):")
    print(f"Tour: {approx_tour} (Distance: {approx_distance})")
    print(f"Time taken (Approximation): {approx_time:.6f} seconds")

if __name__ == "__main__":
    main()

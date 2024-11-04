import random
import time

def quicksort_deterministic(arr):
    """Deterministic variant of Quick Sort using Lomuto partition scheme."""
    if len(arr) <= 1:
        return arr, 0

    pivot = arr[0]  # Choose the first element as pivot
    left = []
    right = []
    comparisons = 0

    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    sorted_left, left_comparisons = quicksort_deterministic(left)
    sorted_right, right_comparisons = quicksort_deterministic(right)

    return sorted_left + [pivot] + sorted_right, comparisons + left_comparisons + right_comparisons


def quicksort_randomized(arr):
    """Randomized variant of Quick Sort."""
    if len(arr) <= 1:
        return arr, 0

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = []
    right = []
    comparisons = 0

    for i in range(len(arr)):
        if i != pivot_index:
            comparisons += 1
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

    sorted_left, left_comparisons = quicksort_randomized(left)
    sorted_right, right_comparisons = quicksort_randomized(right)

    return sorted_left + [pivot] + sorted_right, comparisons + left_comparisons + right_comparisons


def analyze_quick_sort(arr):
    """Analyze the Quick Sort algorithms for a given array."""
    # Analyze deterministic Quick Sort
    start_time = time.time()
    sorted_arr_d, comparisons_d = quicksort_deterministic(arr.copy())
    deterministic_time = time.time() - start_time

    # Analyze randomized Quick Sort
    start_time = time.time()
    sorted_arr_r, comparisons_r = quicksort_randomized(arr.copy())
    randomized_time = time.time() - start_time

    # Results
    print(f"Deterministic Quick Sort: Time = {deterministic_time:.6f}s, Comparisons = {comparisons_d}")
    print(f"Sorted Array (Deterministic): {sorted_arr_d}")
    print(f"Randomized Quick Sort: Time = {randomized_time:.6f}s, Comparisons = {comparisons_r}")
    print(f"Sorted Array (Randomized): {sorted_arr_r}")
    print("-" * 40)


def main():
    n = int(input("Enter the number of elements to sort: "))  # Get number of elements from user
    arr = list(map(int, input(f"Enter {n} integers separated by spaces: ").split()))
    
    if len(arr) != n:
        print(f"Error: Expected {n} integers, but received {len(arr)}.")
        return

    analyze_quick_sort(arr)

if __name__ == "__main__":
    main()

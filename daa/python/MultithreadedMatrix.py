import numpy as np
import threading
import time

# Function for standard matrix multiplication
def matrix_multiply(A, B):
    """Multiply two matrices A and B."""
    n, m = len(A), len(B[0])
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Function for multithreaded matrix multiplication with one thread per row
def multiply_row(A, B, result, row):
    """Multiply one row of matrix A with matrix B."""
    n = len(B[0])
    for j in range(n):
        for k in range(len(B)):
            result[row][j] += A[row][k] * B[k][j]

def matrix_multiply_multithreaded_row(A, B):
    """Multiply two matrices A and B using one thread per row."""
    n, m = len(A), len(B[0])
    result = [[0] * m for _ in range(n)]
    threads = []
    
    for i in range(n):
        thread = threading.Thread(target=multiply_row, args=(A, B, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    return result

# Function for multithreaded matrix multiplication with one thread per cell
def multiply_cell(A, B, result, i, j):
    """Multiply a single cell in the result matrix."""
    for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]

def matrix_multiply_multithreaded_cell(A, B):
    """Multiply two matrices A and B using one thread per cell."""
    n, m = len(A), len(B[0])
    result = [[0] * m for _ in range(n)]
    threads = []
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=multiply_cell, args=(A, B, result, i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
    
    return result

def main():
    # Input for Matrix A
    rows_A = int(input("Enter the number of rows for Matrix A: "))
    cols_A = int(input("Enter the number of columns for Matrix A: "))
    print("Enter the elements of Matrix A row-wise (space-separated):")
    A = []
    for _ in range(rows_A):
        row = list(map(int, input().strip().split()))
        A.append(row)

    # Input for Matrix B
    cols_B = int(input("Enter the number of columns for Matrix B: "))
    print("Enter the elements of Matrix B row-wise (space-separated):")
    B = []
    for _ in range(cols_A):  # B must have the same number of rows as A has columns
        row = list(map(int, input().strip().split()))
        B.append(row)

    print("\nMatrix A:")
    for row in A:
        print(row)
    
    print("\nMatrix B:")
    for row in B:
        print(row)

    # Standard matrix multiplication
    start_time = time.time()
    result_standard = matrix_multiply(A, B)
    standard_time = time.time() - start_time
    print("\nStandard Matrix Multiplication Result:")
    for row in result_standard:
        print(row)
    print(f"Time taken (Standard): {standard_time:.6f} seconds")

    # Multithreaded matrix multiplication (one thread per row)
    start_time = time.time()
    result_row = matrix_multiply_multithreaded_row(A, B)
    row_time = time.time() - start_time
    print("\nMultithreaded Row-wise Matrix Multiplication Result:")
    for row in result_row:
        print(row)
    print(f"Time taken (Row-wise): {row_time:.6f} seconds")

    # Multithreaded matrix multiplication (one thread per cell)
    start_time = time.time()
    result_cell = matrix_multiply_multithreaded_cell(A, B)
    cell_time = time.time() - start_time
    print("\nMultithreaded Cell-wise Matrix Multiplication Result:")
    for row in result_cell:
        print(row)
    print(f"Time taken (Cell-wise): {cell_time:.6f} seconds")

if __name__ == "__main__":
    main()

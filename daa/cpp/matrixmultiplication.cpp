#include <iostream>
#include <vector>
#include <thread>
#include <chrono>

using namespace std;
using namespace chrono;

// Function to initialize a matrix with random values
vector<vector<int>> initializeMatrix(int rows, int cols) {
    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            matrix[i][j] = rand() % 10;  // Random values between 0 and 9
    return matrix;
}

// Single-threaded matrix multiplication
vector<vector<int>> singleThreadedMultiply(const vector<vector<int>> &A, const vector<vector<int>> &B, int N) {
    vector<vector<int>> result(N, vector<int>(N, 0));
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            for (int k = 0; k < N; ++k)
                result[i][j] += A[i][k] * B[k][j];
    return result;
}

// Multithreaded multiplication with one thread per row
void rowMultiply(const vector<vector<int>> &A, const vector<vector<int>> &B, vector<vector<int>> &result, int row, int N) {
    for (int j = 0; j < N; ++j)
        for (int k = 0; k < N; ++k)
            result[row][j] += A[row][k] * B[k][j];
}

vector<vector<int>> multiThreadedRowMultiply(const vector<vector<int>> &A, const vector<vector<int>> &B, int N) {
    vector<vector<int>> result(N, vector<int>(N, 0));
    vector<thread> threads;
    for (int i = 0; i < N; ++i)
        threads.push_back(thread(rowMultiply, ref(A), ref(B), ref(result), i, N));
    for (auto &th : threads)
        th.join();
    return result;
}

// Multithreaded multiplication with one thread per cell
void cellMultiply(const vector<vector<int>> &A, const vector<vector<int>> &B, vector<vector<int>> &result, int row, int col, int N) {
    result[row][col] = 0;
    for (int k = 0; k < N; ++k)
        result[row][col] += A[row][k] * B[k][col];
}

vector<vector<int>> multiThreadedCellMultiply(const vector<vector<int>> &A, const vector<vector<int>> &B, int N) {
    vector<vector<int>> result(N, vector<int>(N, 0));
    vector<thread> threads;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            threads.push_back(thread(cellMultiply, ref(A), ref(B), ref(result), i, j, N));
        }
    }
    for (auto &th : threads)
        th.join();
    return result;
}

int main() {
    int N = 100;  // Matrix dimension (for large matrices, this may take significant time)
    vector<vector<int>> A = initializeMatrix(N, N);
    vector<vector<int>> B = initializeMatrix(N, N);

    // Single-threaded matrix multiplication
    auto start = high_resolution_clock::now();
    vector<vector<int>> resultSingle = singleThreadedMultiply(A, B, N);
    auto end = high_resolution_clock::now();
    auto singleDuration = duration_cast<milliseconds>(end - start);
    cout << "Single-threaded matrix multiplication time: " << singleDuration.count() << " ms" << endl;

    // Multithreaded matrix multiplication with one thread per row
    start = high_resolution_clock::now();
    vector<vector<int>> resultRowThreads = multiThreadedRowMultiply(A, B, N);
    end = high_resolution_clock::now();
    auto rowThreadDuration = duration_cast<milliseconds>(end - start);
    cout << "Multithreaded matrix multiplication (one thread per row) time: " << rowThreadDuration.count() << " ms" << endl;

    // Multithreaded matrix multiplication with one thread per cell
    start = high_resolution_clock::now();
    vector<vector<int>> resultCellThreads = multiThreadedCellMultiply(A, B, N);
    end = high_resolution_clock::now();
    auto cellThreadDuration = duration_cast<milliseconds>(end - start);
    cout << "Multithreaded matrix multiplication (one thread per cell) time: " << cellThreadDuration.count() << " ms" << endl;

    return 0;
}

#include <iostream>
#include <vector>
#include <thread>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

// Merge function for merge sort
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; ++i)
        L[i] = arr[left + i];
    for (int i = 0; i < n2; ++i)
        R[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];
}

// Single-threaded merge sort
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Multithreaded merge sort
void threadedMergeSort(vector<int>& arr, int left, int right, int depth = 0) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        if (depth < 4) {  // Limit depth of threading to avoid overhead
            thread t1(threadedMergeSort, ref(arr), left, mid, depth + 1);
            thread t2(threadedMergeSort, ref(arr), mid + 1, right, depth + 1);
            t1.join();
            t2.join();
        } else {
            threadedMergeSort(arr, left, mid, depth + 1);
            threadedMergeSort(arr, mid + 1, right, depth + 1);
        }
        
        merge(arr, left, mid, right);
    }
}

int main() {
    int n = 100000;  // Array size for testing (can adjust for performance testing)
    vector<int> arr1(n), arr2(n);

    // Initialize best-case scenario (sorted array)
    for (int i = 0; i < n; i++) {
        arr1[i] = i;
        arr2[i] = i;
    }

    // Measure time for single-threaded merge sort in best case
    auto start = high_resolution_clock::now();
    mergeSort(arr1, 0, n - 1);
    auto end = high_resolution_clock::now();
    auto singleThreadedDurationBest = duration_cast<milliseconds>(end - start);
    cout << "Single-threaded merge sort (best case): " << singleThreadedDurationBest.count() << " ms" << endl;

    // Measure time for multithreaded merge sort in best case
    start = high_resolution_clock::now();
    threadedMergeSort(arr2, 0, n - 1);
    end = high_resolution_clock::now();
    auto multiThreadedDurationBest = duration_cast<milliseconds>(end - start);
    cout << "Multithreaded merge sort (best case): " << multiThreadedDurationBest.count() << " ms" << endl;

    // Initialize worst-case scenario (reverse sorted array)
    for (int i = 0; i < n; i++) {
        arr1[i] = n - i;
        arr2[i] = n - i;
    }

    // Measure time for single-threaded merge sort in worst case
    start = high_resolution_clock::now();
    mergeSort(arr1, 0, n - 1);
    end = high_resolution_clock::now();
    auto singleThreadedDurationWorst = duration_cast<milliseconds>(end - start);
    cout << "Single-threaded merge sort (worst case): " << singleThreadedDurationWorst.count() << " ms" << endl;

    // Measure time for multithreaded merge sort in worst case
    start = high_resolution_clock::now();
    threadedMergeSort(arr2, 0, n - 1);
    end = high_resolution_clock::now();
    auto multiThreadedDurationWorst = duration_cast<milliseconds>(end - start);
    cout << "Multithreaded merge sort (worst case): " << multiThreadedDurationWorst.count() << " ms" << endl;

    return 0;
}

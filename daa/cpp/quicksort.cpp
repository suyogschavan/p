#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int deterministicPartition(vector<int> &arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void deterministicQuickSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pi = deterministicPartition(arr, low, high);
        deterministicQuickSort(arr, low, pi - 1);
        deterministicQuickSort(arr, pi + 1, high);
    }
}

int randomizedPartition(vector<int> &arr, int low, int high) {
    int randomIndex = low + rand() % (high - low + 1);
    swap(arr[randomIndex], arr[high]);
    return deterministicPartition(arr, low, high);
}

void randomizedQuickSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pi = randomizedPartition(arr, low, high);
        randomizedQuickSort(arr, low, pi - 1);
        randomizedQuickSort(arr, pi + 1, high);
    }
}

int main() {
    int n = 10000;
    vector<int> arr1(n), arr2(n);
    for (int i = 0; i < n; i++) {
        arr1[i] = rand() % 10000;
        arr2[i] = arr1[i];
    }

    auto start = high_resolution_clock::now();
    deterministicQuickSort(arr1, 0, n - 1);
    auto end = high_resolution_clock::now();
    auto deterministicDuration = duration_cast<milliseconds>(end - start);
    cout << "Time taken by Deterministic QuickSort: " << deterministicDuration.count() << " ms" << endl;

    start = high_resolution_clock::now();
    randomizedQuickSort(arr2, 0, n - 1);
    end = high_resolution_clock::now();
    auto randomizedDuration = duration_cast<milliseconds>(end - start);
    cout << "Time taken by Randomized QuickSort: " << randomizedDuration.count() << " ms" << endl;

    if (arr1 == arr2) {
        cout << "Both algorithms sorted the array correctly!" << endl;
    } else {
        cout << "The algorithms produced different results." << endl;
    }

    return 0;
}

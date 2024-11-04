#include<bits/stdc++.h>
using namespace std;

int solve01Knapsack(vector<int> weights, vector<int> profits, int w, int n){
    if(n==0 || w==0) return 0;

    if(weights[n]>w) return solve01Knapsack(weights, profits, w, n-1);

    return max(profits[n]+solve01Knapsack(weights, profits, w-weights[n], n-1), solve01Knapsack(weights, profits, w, n-1));
}

int main(){
    vector<int> weights;
    vector<int> profits;
    int n, w;
    cout<<"Enter the number of elements: ";
    cin>>n;
    for(auto i=0; i<n; i++){
    int weight, profit;
        cin>>weight>>profit;
        weights.push_back(weight);
        profits.push_back(profit);
    }

    cout<<"Enter the maximum capacity : ";
    cin>>w;

    cout<<"Max profit : "<<solve01Knapsack(weights, profits, w, n);

}
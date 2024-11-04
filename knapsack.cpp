#include<bits/stdc++.h>
using namespace std;

class Obj{
    public:
    int profit, weight;
    Obj(int p, int w){
        this->profit = p;
        this->weight = w;
    }
};

int main(){
    int t, n;
    cout<<"Enter the number of objects: ";
    cin>>n;
    t = n;
    cout<<"Enter the profit and weight : "<<endl;
    vector<pair<float, Obj*>>items; // MaxHeap
    while(t--){
        int p,w;
        cin>>p>>w;
        Obj* o = new Obj(p,w);
        items.push_back({(float)p/w, o});
    }
    sort(items.begin(), items.end(), greater<pair<float,Obj*>>());
    int maxCapacity;
    cout<<"Enter the maximum capacity of knapsack: ";
    cin>>maxCapacity;

    float totalProfit = 0;

    for(auto i:items){
        if(maxCapacity == 0) break;
        if(i.second->weight <= maxCapacity){
            maxCapacity -= i.second->weight;
            totalProfit += i.second->profit;
        }else{
            totalProfit += i.second->profit * ((float)maxCapacity /(float)i.second->weight);
            maxCapacity = 0;
        }
    }

    cout<<"totalProfit: "<<totalProfit<<endl;
}
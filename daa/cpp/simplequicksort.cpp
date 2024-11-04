#include<bits/stdc++.h>
using namespace std;

int quickSort(vector<int>& v, int low, int high){
    int pivote = v[low];
    int i,j;
    i=low;
    j=high;
    while(i<j){
        while(v[i] <= pivote && i<high) i++;
        while(v[j] > pivote && j>low) j--;
        if(i<j)
        swap(v[i], v[j]);
    }
    swap(v[low], v[j]);
    return j;
}

void reccursion(vector<int> &v, int low, int high){
    if(low<high){
        int pIndex = quickSort(v, low, high);
        reccursion(v, low, pIndex-1);
        reccursion(v, pIndex+1, high);
    }    
}


int main(){
    vector<int> v = {4, 6, 2, 5, 7, 9, 1, 3};
    reccursion(v, 0, v.size()-1);
    for(auto i:v) cout<<i<<" ";

}
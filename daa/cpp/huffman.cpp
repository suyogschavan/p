#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    char val;
    Node* left;
    Node* right;
    Node(char c){
        this->val = c;
        left = nullptr;
        right = nullptr;
    }
};
    
void printVector(vector<int> v){
    for(auto i:v){
        cout<<i<<" ";
    }
}

void printCodes(Node* root, vector<int>& v){
    if(root->left){
        v.push_back(0);
        printCodes(root->left, v);
        v.pop_back();
    }
    if(root->right) {
        v.push_back(1);
        printCodes(root->right, v);
        v.pop_back();
    }
    if(root->left == nullptr && root->right == nullptr){
        cout<<root->val<<" -> ";
        printVector(v);
        cout<<endl;
    }
}



void huffman(string s){
    unordered_map<char, int> mp;
    for(auto i:s) mp[i]++;

    priority_queue<pair<int, Node*>, vector<pair<int, Node*>>, greater<pair<int,Node*>>> minheap;
    for(auto i:mp){
        Node* newNode = new Node(i.first);
        minheap.push({i.second, newNode});
    }

    while(minheap.size()> 1){
        int a = minheap.top().first;
        auto node1 = minheap.top().second;
        minheap.pop();
        int b = minheap.top().first;
        auto node2 = minheap.top().second;
        minheap.pop();

        Node* newHead = new Node('$');
        newHead->left = node1;
        newHead->right = node2;
        minheap.push({a+b, newHead});
    }

    auto head = minheap.top().second;
    vector<int> v;
    printCodes(head, v);
}

int main(){
    string s;
    cout<<"Enter the string : ";
    cin>>s;

    huffman(s);
    return 0;
}
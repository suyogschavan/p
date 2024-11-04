#include<bits/stdc++.h>
using namespace std;
int n;
unordered_set<int> column;
unordered_set<int> posDiag;
unordered_set<int> negDiag;
vector<vector<vector<char>>> answer;


void backtrack(int row, vector<vector<char>>& board){
    if(row == n) {
        answer.push_back(board);
        return;
    }

    for(int col = 0; col<n; col++){
        if(column.count(col) || posDiag.count(col+row) || negDiag.count(row-col)) continue;
        column.insert(col);
        posDiag.insert(col+row);
        negDiag.insert(row-col);
        board[row][col]='Q';
        backtrack(row+1, board);
        board[row][col]='.';
        column.erase(col);
        posDiag.erase(row+col);
        negDiag.erase(row-col);
    }
}

void printAnswer(vector<vector<vector<char>>>& answer){
    if(answer.size()>0){
        cout<<"No. of solutions: "<<answer.size()<<endl;
        cout<<"__________\n Solutions: "<<endl;
        for(auto board:answer){
            for(auto i:board){
                for( auto c:i){
                    cout<<c<<" ";
                }
                cout<<endl;
            }
            cout<<"______________"<<endl;
        }
    }else{
        cout<<"No solution exists for this placement of queen "<<endl;
    }
}

int main(){
    cout<<"Enter N: ";
    cin>>n;
    cout<<"Enter the coordinates: ";
    int row, col;
    cin>>row>>col;
    if(row>=n || col>=n) {
        cout<<"Invalid coordinates: "<<endl;
        return 0;
    }
    vector<vector<char>> board(n, vector<char>(n, '.'));

    column.insert(col);
    posDiag.insert(row+col);
    negDiag.insert(row-col);
    board[row][col] = 'q';

    backtrack(row+1, board);
    printAnswer(answer);
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> dice;
    int prize;
    int x;
    for (int i = 0; i < 3; ++i){
        cin>>x;
        dice.push_back(x);
    }
    
    sort(dice.begin(), dice.end());

    if (dice[0] == dice[2]){
        prize = 10000 + 1000*dice[0];
    }
    else if (dice[0] == dice[1]) {
        prize = 1000 + 100*dice[0];
    }
    else if (dice[1] == dice[2]) {
        prize = 1000 + 100*dice[1];
    }
    else {
        prize = 100*dice[2];
    }
    cout << prize << endl;

}
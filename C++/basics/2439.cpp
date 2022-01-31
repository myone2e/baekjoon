#include <iostream>
using namespace std;
// C++ 은 파이썬처럼 '*'*5 안됨!

int main() {
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++){
        for (int j = N; j > i; j--){
            cout << ' '; // no endl
        }
        for (int k = 1; k <= i ; k++){
            cout << '*'; // no endl => 별 하나 찍고 끝내버림
        }
        cout << endl;
    }
}
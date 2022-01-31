#include <iostream>
using namespace std;

int main() {
    int N, X, n;
    cin >> N >> X;
    for (int i = 0 ; i < N ; i ++){
        cin >> n;
        if (n < X){ //조건문 형식 (조건) {} 형식 
            cout << n << ' ';
        }
    }
}
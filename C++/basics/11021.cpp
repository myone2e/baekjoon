#include <iostream>
using namespace std;

int main(){
    int T, A, B;
    cin >> T;
    for (int i = 0; i < T; i++){ // 초기 조건; 반복 조건; 증감
        cin >> A >> B; 
        cout << "Case #" << i+1 << ": "<< A+B << endl;
    }
}
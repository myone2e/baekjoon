#include <iostream>
using namespace std;

int main() {
    int N, sum, result;
    cin >> N;
    int cnt = 0;

    if (N < 10){
        N *= 10;
    }
    result = N;

    while (true){
        sum = (result/10) + (result%10); // int라서 /해도 몫
        result = (result % 10)*10 + (sum%10); //괄호 안하면 더해지고 나머지 계산됨!
        cnt ++;

        if (N == result){
            break;
        }
    }
    cout << cnt;
}
#include <iostream>
using namespace std;

int main() {
    int arr[42] = {};

    int n;
    for (int i = 0; i < 10; i++){
        cin >> n;
        arr[n%42]++;
    }

    int cnt = 0;

    for (int j = 0; j < 42; j ++){
        if (arr[j] > 0){
            cnt ++;
        }
    }
    cout << cnt;
}
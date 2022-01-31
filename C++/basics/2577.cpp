#include <iostream>
using namespace std;

int main() {
    int A, B, C, ABC;
    cin >> A >> B >> C;

    ABC = A*B*C;

    int arr[10] = {};

    while (ABC>0){
        arr[ABC%10]++;

        ABC /= 10;

    }
    for (int i = 0 ; i < 10 ; i ++){
        cout << arr[i] << endl;
    }

}
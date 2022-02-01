#include <iostream>
#include <algorithm> //sort 쓰려고
using namespace std;

int main() {
    int N;
    cin >> N;
    double sum = 0;

    double arr[1001] = {};
    for (int i = 0; i < N; i++){
        cin >> arr[i]; //이런 식으로 입력 받기 가능
    }

    sort(arr, arr + N); //Sorts the elements in the range [first,last) into ascending order.
    //arr[0] ~ arr[0+N]

    for (int j = 0; j < N; j++){
        sum = sum + (arr[j]/arr[N-1])*100;
    }
    double avg = sum / N;
    
    cout << avg;

}
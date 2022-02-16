#include <iostream>
using namespace std;

int main() {
    int hour, minute, cook;
    int m;
    cin >> hour >> minute;
    cin >> cook; // input 줄이 바뀌면 cin도 바꿔주기

    m = minute + cook;

    while (m > 59){
        ++hour;
        m -= 60;
    }
    if (hour >= 24) hour %= 24; // 나머지를 대입
    cout << hour << " "<< m <<endl;
}
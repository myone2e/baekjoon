#include <iostream>

// 파이썬처럼 '3' in str 안됨
bool check(int h, int m, int s) {
    if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3) // 앞자리 뒷자리
        return true;
    return false;
}
int h;
int cnt = 0;

int main() {
    
    std::cin>>h;
    for (int i = 0; i <= h; ++i){
        for (int j = 0; j < 60; ++j){
            for (int k = 0; k < 60; ++k){
                if (check(i,j,k)) ++cnt;
            }
        }
    }
    std::cout<<cnt<<'\n';
    return 0;
}
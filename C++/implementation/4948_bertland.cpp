// 시간 초과

#include <iostream>
#include <cmath>

bool CheckPrime(int n){
    if (n==1) return false;
    else{
        for (int i = 2; i <= std::pow(n, 0.5); ++i) { // if <=, no + 1 at the end!
            if (n%i==0) return false;
        }
    }
    return true;
}

int main() {
    int n;
    while (std::cin>>n){
        int cnt = 0;
        if (n==0) break;
        for (int i = n; i<=2*n; ++i){
            if (CheckPrime(i)) ++cnt;
        }
        std::cout<<cnt<<std::endl;
    }
    return 0;
}


#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

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
    int N;
    std::cin>>N;

    if (CheckPrime(N)){
        std::cout<<N<<std::endl;
        return 0;
    }
    else{
        for (int i = 2; i <= pow(N,2); ++i){
            while (N%i == 0){
                std::cout<<i<<std::endl;
                N /= i;
            }
        }
    }
    return 0;
}
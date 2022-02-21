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
    int M, N;
    std::cin>>M;
    std::cin>>N;

    std::vector<int> vec;

    for (int j = M; j <= N; ++j) {
        if (CheckPrime(j)) vec.push_back(j);
    }

    if (vec.size() == 0) std::cout<<-1<<std::endl;
    else{
        std::cout<<std::accumulate(vec.begin(), vec.end(), 0)<<std::endl;
        std::cout<<vec[0]<<std::endl;
    }

}
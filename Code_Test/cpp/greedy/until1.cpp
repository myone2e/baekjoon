#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    int N, K;
    std::cin>>N>>K;
    int cnt = 0;
    while (N!=1){
        if (N%K == 0){
            N /= K;
            ++cnt;
        }
        else{
            N -= 1;
            ++cnt;
        }
    }
    std::cout<<cnt<<'\n';
    return 0;
}
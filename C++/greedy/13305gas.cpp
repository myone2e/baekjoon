#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    int N;
    long long x;
    std::cin>>N;
    std::vector<long long> dist;
    for (int i = 0; i < N-1; ++i){
        std::cin>>x;
        dist.push_back(x);
    }

    std::vector<long long> price;
    for (int i = 0; i < N; ++i){
        std::cin>>x;
        price.push_back(x);
    }

    long long result = 0;
    long long min_price = price[0];
    result += price[0]*dist[0]; 

    for (int i = 1; i < price.size()-1; ++i){
        if (price[i] > min_price){
            result += min_price * dist[i];
        }
        else{
            min_price = price[i]; 
            result += min_price*dist[i];
        }
    }

    std::cout<<result<<'\n';
    return 0;

    // 일단 한 번 가고
    // 다음 가격이 크면 미리 넣고
    // 아니면 가서 넣고!
    // vector<int> vec(3) => 0 0 0 
    // vector<int> vec(3, -1) => -1 -1 -1
}
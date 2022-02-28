#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    int N, M, K; // N: array len, M: # of + , # K: max usage per once
    std::cin>>N>>M>>K;
    int x;
    std::vector<int> v(N);
    for (int i = 0 ; i < N; ++i){
        std::cin>>x;
        v.push_back(x);
    }

    sort(v.begin(), v.end());

    int first = v[v.size()-1];
    int second = v[v.size()-2];

    // first: M을 K+1 뭉텅이로 나눈 몫 중 K번씩 + 나머지는 전부 K
    int cnt = int(M / (K+1)) * K;
    cnt += M%(K+1);
    int result = 0;
    result += cnt * first;
    result += (M - cnt)*second;
    
    std::cout<<result<<'\n';
}
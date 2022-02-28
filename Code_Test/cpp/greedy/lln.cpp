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
    int result = 0;

    while (true) {
        // 가장 큰 수를 K 번 더하고
        for (int i = 0; i < K; ++i){
            if (M==0) break;
            result += first;
            M -= 1;
        }
        if (M == 0) break;
        // 두 번째로 큰 걸 한 번 더하고 다시 while 돌리기
        result += second;
        M -= 1;
    }
    std::cout<<result<<'\n';
}
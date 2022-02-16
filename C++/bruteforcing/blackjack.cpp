#include <iostream>
#include <vector>

int main() {
    int N, M;
    std::vector<int> nums;
    std::cin >> N >> M;
    int x;
    for (int i = 0; i < N; ++i) {
        std::cin>>x;
        nums.push_back(x);
    }

    int max = 0;
    int sum = 0;
    for (int i = 0; i < N-2; ++i){
        for (int j = i+1; j < N-1; ++j){
            for (int k = j + 1; k < N; ++k){
                sum = nums[i] + nums[j] + nums[k];
                if (sum > max && sum <= M){
                    max = sum;
                }
            }
        }
    }
    std::cout<<max<<std::endl;

}
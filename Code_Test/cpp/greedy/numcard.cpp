#include <vector>
#include <iostream>
#include <algorithm>

int r, c;

int main() {
    std::cin>>r>>c;
    int x;
    int result = 0;
    for (int i = 0; i < r; ++i){
        std::vector<int> v;
        for (int j = 0; j < c; ++j){
            std::cin>>x;
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        result = std::max(result, v[0]);
    }
    std::cout<<result<<'\n';
    return 0;
}
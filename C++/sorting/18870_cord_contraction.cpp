#include <vector>
#include <algorithm>
#include <iostream>

std::vector<int> not_in_place_sort(std::vector<int> original) { // inplace = false vector 
    std::sort(original.begin(), original.end());
    return original;
}

int main() {
    int n, x;
    std::cin>>n;
    std::vector<int> vec;

    for (int i = 0; i < n; ++i){
        std::cin>>x;
        vec.push_back(x);
    }
    std::vector<int> v_sorted = not_in_place_sort(vec); 

    int cnt = 0;
    for (int j = 0; j < vec.size(); ++j){
        if (vec[j] == v_sorted[j]){
            std::cout<<cnt;
            continue;
        }
        else ++cnt;
    }

}
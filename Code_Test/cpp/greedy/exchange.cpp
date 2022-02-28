#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin>>n;
    
    int cnt = 0;
    std::vector<int> coin = {500, 100, 50, 10};

    for (int i = 0; i < coin.size(); ++i){
        cnt += n / coin[i];
        n %= coin[i];
    }
    std::cout << cnt << '\n';
}
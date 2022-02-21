#include <iostream>
#include <vector>
// k 층 n 호 = k-1 층의 1호부터 n 호까지의 합 = k-1 층의 n 호와 k 층의 n-1 호의 합

int fillFloor(int k, int n) {
    if (n==1) return 1;
    if (k==0) return n;
    return (fillFloor(k-1, n) + fillFloor(k, n-1));
}
int main() {
    int T, k, n;
    std::vector<int> floor;
    std::cin >> T;
    for (int i = 0; i < T; ++i){
        std::cin>>k;
        std::cin>>n;

        std::cout<<fillFloor(k,n)<<std::endl;
    }
}
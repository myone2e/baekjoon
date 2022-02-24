#include <iostream>

int main() {
    int L, P; // L: People per 1m^2, P: Total area
    std::cin>>L>>P;
    int total = L*P;

    int x;
    int diff;
    for (int i = 0; i < 5 ; ++i){
        std::cin>>x;
        diff = x - total;
        std::cout<<diff<<" ";
    }
    std::cout<<std::endl;
    return 0;
}
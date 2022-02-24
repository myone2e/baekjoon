#include <vector>
#include <iostream>
#include <cmath>

int main() {
    int T;
    std::cin>>T;

    int x_1, y_1, r_1, x_2, y_2, r_2;

    for (int i = 0; i < T; ++i){
        std::cin>>x_1>>y_1>>r_1>>x_2>>y_2>>r_2;
        double distance = pow(pow(x_1 - x_2 , 2) + pow(y_1 - y_2, 2), 0.5);
        if (distance == 0 && r_1 == r_2) std::cout<<-1<<std::endl;
        else if (abs(r_1-r_2) == distance || (r_1 + r_2) == distance) std::cout<<1<<std::endl;
        else if (abs(r_1-r_2) < distance && distance < (r_1+r_2)) std::cout<<2<<std::endl;
        else{
            std::cout<<0<<std::endl;
        }
    }
    return 0;
}
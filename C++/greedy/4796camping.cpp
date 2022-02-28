#include <iostream>

int main() {
    int L, P, V;
    int result = 0;
    int i = 0;
    while (true){
        std::cin>>L>>P>>V;
        if (L==0 && P == 0 && V == 0){
            break;
        }
        result = (V / P) * L + std::min(V % P, L); // min use + 나머지
        std::cout << "Case " << ++i << ": " << result << "\n";
    }
    return 0;
}
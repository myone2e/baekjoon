#include <vector>
#include <algorithm>
#include <iostream>

std::vector<int> not_in_place_sort(std::vector<int> original) { // inplace = false vector 
    std::sort(original.begin(), original.end());
    return original;
}
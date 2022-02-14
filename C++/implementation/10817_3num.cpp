#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> vec;
    int x;
    while (cin>>x){
        vec.push_back(x);
    }
    sort(vec.begin(), vec.end());
    cout<<vec[1]<<endl;
}
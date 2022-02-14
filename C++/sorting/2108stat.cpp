#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int mean(vector<int> &vec){
    int sum=0, cnt=0;
    for (int i = 0; i < vec.size(); ++i){
        sum = sum + vec[i];
        ++cnt;
    }
    return sum/cnt;
}
double median(vector<int> &vec){
    sort(vec.begin(), vec.end()); // 5개 => 3번째 mid = 2 // 6개 => 3, 4번째 2,3 으로 평균
    int mid;
    if (vec.size()%2==0) { // if even size
        mid = vec.size()/2;
        return (vec[mid-1] + vec[mid]) / 2;
    }
    else {
        mid = (vec.size()-1) / 2;
        return vec[mid];
    }
}

int mode(vector<int> &vec){
    
}

int range(vector<int> &vec) {
    sort(vec.begin(), vec.end());
    int r;
    r = vec[vec.size()-1] - vec[0];
    return r;
}

int main(){
    vector<int> vec;
    int x;
    while (cin>>x){
        vec.push_back(x);
    }

}

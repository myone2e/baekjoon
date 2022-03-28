#include <iostream>
#include <stack>
// LIFO (stack on the top of the tower)
std::stack<int> s; // how to use stack

int main(){
    // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();

    while (!s.empty()){
        std::cout<<s.top()<<' '; // print the top element
        s.pop(); // delete the top element
    }
}

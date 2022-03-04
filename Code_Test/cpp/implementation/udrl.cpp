#include <iostream>
#include <string>

int main(){

    int x = 1;
    int y = 1;
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    char moves[] = {'L', 'R', 'U', 'D'};
    int N;
    std::cin>>N;
    std::string commands;
    std::cin.ignore(); // clear the buffer (for strings)
    getline(std::cin, commands); // how to read inputs

    for (int i = 0; i < commands.size(); ++i) {
        char command = commands[i];

        int nx, ny; // declare
        for (int j = 0; j < 4; ++j){
            if (command == moves[j]){
                nx = x + dx[j];
                ny = y + dy[j];
            }
        }

        if (nx < 1 || ny < 1 || nx > N || ny > N) continue;

        x = nx;
        y = ny;
    }
    std::cout << x << ' ' << y << '\n';
    return 0;
}
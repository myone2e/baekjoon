# working

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # num col, num row # M x N matrix

dx = [0,0,1,-1]
dy = [1,-1,0,0]

temp = []
for _ in range(N):
    temp.append(list(map(int, input().split())))
    
graph = [[0]*N for _ in range(M)] # Generate M x N matrix

for i in range(N):
    for j in range(M):
        if temp[i][j] != -1:
            graph[i][j] = 1


        
print(temp)
print(graph)

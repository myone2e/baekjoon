import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # num col, num row
n, m = N, M # n x m matrix
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 1 인 지점 (virus 개념)을 모두 넣고 시작. 한 번에 퍼지기 때문
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

day = -1          # 전부 1이면 밑에 다 돌고 -1 + 1 = 0 return # 뭐라도 큐에 있으면 +1 되서 마지막 날까지 카운트 됨
def bfs(graph):
    global day
    while queue:
        day += 1
        for _ in range(len(queue)): # 1로 시작하는 (감염된 애들 수 만큼)
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1 # 새로 전파
                    queue.append((nx,ny)) # 새로 익은 애들을 전부 큐에 넣어줌  
    return graph

box = bfs(graph)
for row in box:
    if 0 in row:
        print(-1)
        break
else:
    print(day)
        
        
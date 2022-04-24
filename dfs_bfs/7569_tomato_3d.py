import sys
from collections import deque
input = sys.stdin.readline

M, N, h = map(int, input().split()) # num col, num row # number of floors
n, m = N, M # n x m matrix

graph = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

dz = [-1,1,0,0,0,0]
dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]

queue = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                queue.append((k,i,j))

day = -1          # 전부 1이면 밑에 다 돌고 -1 + 1 = 0 return # 뭐라도 큐에 있으면 +1 되서 마지막 날까지 카운트 됨
def bfs(graph):
    global day
    while queue:
        day += 1
        for _ in range(len(queue)): # 1로 시작하는 (감염된 애들 수 만큼)
            z, x, y = queue.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                    continue
                if graph[nz][nx][ny] == -1:
                    continue
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1 # 새로 전파
                    queue.append((nz,nx,ny)) # 새로 익은 애들을 전부 큐에 넣어줌  
    return graph

cube = bfs(graph)

flag = False
for box in cube:
    if flag == True:
        break
    for row in box:
        if 0 in row:
            print(-1)
            flag = True
            break
if flag == False:
    print(day)
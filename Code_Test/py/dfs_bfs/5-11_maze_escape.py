from collections import deque
import sys
input = sys.stdin.readline
# 1로 이루어진 오른쪽 하단으로 나가는 최단경로 찾기

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().strip()))) # input이 00110 이렇게 들어와서 split x

# 이동할 방향 pair (상, 하, 좌, 우 ! y가 뒤로 즉 몇 열을 의미함!)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어난다면 무시
            if nx<0 or ny < 0 or nx >= n or ny >= m: # [0, n)이라서 = 붙음
                continue
            # 벽이라면 무시
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 길이라면 + 1 해서 표시
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[n-1][m-1] # (n,m)에서 종료

print(bfs(0,0)) # (1,1) 위치에서 출발

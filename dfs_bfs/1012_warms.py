from collections import deque
import sys
input = sys.stdin.readline

# 이동할 방향 pair (상, 하, 좌, 우 ! y가 뒤로 즉 몇 열을 의미함!)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작합니다.

# 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고

# 한 번의 BFS가 끝나게 되면 더 이상 확장이 불가능 하므로 구역 하나가 탄생합니다.

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:  # 0으로 만들어서 다시 오지 않도록 & 다른 i,j bfs에서 오지 않도록
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t): # loop through test cases
    cnt = 0
    n, m, k = map(int,input().split()) # n x m matrix
    graph = [[0]*m for _ in range(n)] # Generate n x m matrix 

    for j in range(k): # k: number of coordinates
        x, y = map(int, input().split()) # input = coordinate
        graph[x][y] = 1 # mark the inputs

    for a in range(n): # don't know the starting point => loop all
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1 # one bfs => 1 cnt
    print(cnt)
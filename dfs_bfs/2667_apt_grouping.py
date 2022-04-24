from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

# 이동할 방향 pair (상, 하, 좌, 우 ! y가 뒤로 즉 몇 열을 의미함!)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작합니다.

# 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고

# 한 번의 BFS가 끝나게 되면 더 이상 확장이 불가능 하므로 마을 하나가 탄생합니다.

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1 # cnt for houses

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 0으로 만들어서 다시 오지 않도록 & 다른 i,j bfs에서 오지 않도록
                queue.append((nx, ny))
                cnt += 1
    return cnt

counts = [] # counts for storage
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 앞에서 이미 0으로 만든 구역은 실행되지 않음!
            counts.append(bfs(graph, i, j))
            
counts.sort() 
print(len(counts)) # how many villages
for i in range(len(counts)):
    print(counts[i])

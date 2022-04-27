from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로 크기 = 행 수, 가로 크기

graph = [] # adjacency matrix (only coordinates)
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 방향 pair (상, 하, 좌, 우 ! y가 뒤로 즉 몇 열을 의미함!)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs part
max_safe = 0
def spread_virus():
    global max_safe
    
    graph_copy = copy.deepcopy(graph) # 그래프 복사
    
    # 바이러스를 전부 큐에 삽입
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            # 빈 곳에는 바이러스 전파
            if graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = 2
                queue.append((nx,ny))
    # 단순히 0인 영역 찾기
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 0:
                safe_area += 1
    max_safe = max(max_safe, safe_area)
    
# Brute Force 
def build_wall(cnt): # 나중에 0을 넣어서 시작
    if cnt == 3:
        spread_virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                print('+1 wall') # 이게 졸라 많이 찍힘
                build_wall(cnt+1) # 얘가 실행되도 돌아올 때 포문은 계속 돔
                graph[i][j] = 0 # 벽이 세워진 채로 copy됨. 다시 돌려놔야 다 탐색 가능
                print('return 1 wall') # +1  return 1 wall 이 번갈아 가면서 계속 찍힘
build_wall(0)
print(max_safe)
        
    
    
    



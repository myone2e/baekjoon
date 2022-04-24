import sys
input = sys.stdin.readline
# 0으로 이루어진 area 찾기
# 여기는 단지와 반대로 1로 만들고 0이면 bfs 수행

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().strip()))) # input이 00110 이렇게 들어와서 split x

print(graph)

def dfs(x, y):
    # 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return 0
    if graph[x][y] == 0: # 현재 노드 방문한 적이 없다면
        graph[x][y] = 1 # 방문처리하고
        dfs(x - 1, y) # 좌
        dfs(x, y - 1) # 하
        dfs(x + 1, y) # 우
        dfs(x, y + 1) # 상
        return 1 # count += 1
    return 0

result = 0
# 0,0 부터 시작
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == 1: # 1을 만나면 count += 1
            result += 1

print(result)
print(graph)
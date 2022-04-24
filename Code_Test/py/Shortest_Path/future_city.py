import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)] # n+1 x n+1 matrix

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 거리가 무조건 1이기 때문에 ! 앞에서의 c는 주어지지 않음
    graph[b][a] = 1

x, k = map(int, input().split()) # 목표, 중간 지점

for k in range(1, n+1): # for n nodes (거쳐 가는 노드로)
    for a in range(1, n+1): # starting point
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # direct or pass through

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)

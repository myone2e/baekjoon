INF = int(1e9)

n = int(input()) # number of vertices
m = int(input()) # number of edges

# 2 dim list (graph)
graph = [[INF]*(n+1) for _ in range(n+1)]

# Set diagonal to zero (self to self)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# Receive info of edges
for _ in range(m): 
    a, b, c = map(int, input().split()) # start, end, dist
    if graph[a][b] > c: # 하나 이상의 경로가 주어질 수 있는 조건 존재
        graph[a][b] = c

for k in range(1, n+1): # for n nodes (거쳐 가는 노드로):
    for a in range(1, n+1): # starting point
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # direct or pass through

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()

print()

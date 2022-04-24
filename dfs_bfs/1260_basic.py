import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    node, value = map(int, input().split())
    graph[node].append(value)
    graph[value].append(node)

# sort adjacency list # 동일 거리일 경우 낮은 번호 순으로 작동하도록!
for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # 1번 노드 => 연결된 애들 순서대로
        if not visited[i]: # 방문 안했으면
            dfs(graph, i, visited) # 거기서 다시 깊게

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    #큐가 빌 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]: # 연결된 애들
            if not visited[i]: # 방문 안했다면
                queue.append(i) # 큐에 넣고 => 얘가 다음 순서 v
                visited[i] = True # 방문처리

dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(graph, V, visited)
print()


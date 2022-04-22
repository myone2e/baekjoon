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
    for i in graph[v]: # 1번 노드 => 2, 3, 8 순서대로
        if not visited[i]: # if visitied[i] == 0
            dfs(graph, i, visited) ## i가 다시 v로

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    #큐가 빌 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결되고 아직 방문하지 않은 원소를 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(graph, V, visited)
print()


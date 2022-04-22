import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
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
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # 1번 노드 => 2, 3, 8
        if not visited[i]:
            dfs(graph, i, visited) ## i가 다시 v로 들어가는 구조!
    return sum(visited) - 1

print(dfs(graph, 1, visited))


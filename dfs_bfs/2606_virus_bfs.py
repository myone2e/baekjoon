from collections import deque
import sys
input = sys.stdin.readline

# virus 

n = int(input()) # number of computers (vertices)
m = int(input()) # number of edges
graph = [[] for _ in range(n+1)] # to make it easy
for _ in range(m): # as number of edges
    v1, v2 = map(int,input().split())
    graph[v1].append(v2) # append! not =
    graph[v2].append(v1)
    
# sort adjacency list # 동일 거리일 경우 낮은 번호 순으로 작동하도록!
for i in range(1, n+1):
    graph[i].sort()

def bfs(graph, start, visited): # visited = [0] * (n + 1)
    queue = deque([start])
    visited[start] = True
    while queue: # 큐가 빌 때 까지
        v = queue.popleft()
        
        for i in graph[v]: # 연결된 애들 확인
            if not visited[i]:
                queue.append(i) # 큐에 넣고
                visited[i] = True # 방문처리
                
    return sum(visited) - 1

visited = [0] * (n+1)
print(bfs(graph, 1, visited))
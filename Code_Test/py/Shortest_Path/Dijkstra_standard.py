import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # num vertices, num edges
start = int(input())

graph = [[] for i in range(n+1)] # +1 for indexing (vertex starts at 1)
visited = [False] * (n+1)
distance = [INF] * (n+1) # shortest distance table

# receive edges
for _ in range(m):
    a, b, c = map(int, input().split()) # from a to b , distance is c 
    graph[a].append((b,c)) # distance may vary between two nodes
    
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q) # 가장 가까운 노드에 대한 정보 꺼내기 (거리, 노드 번호)
        
        if distance[now] < dist: # table 거리보다 길다면 (이미 처리된 거라면) => 무시
            continue
        
        for i in graph[now]: # 현재 노드와 연결된 애들애 대해서
            cost = dist + i[1] # 현재 노드를 거쳐 가는 거리 계산하고

            if cost < distance[i[0]]: # 바로 가는 것 보다 짧다면
                distance[i[0]] = cost # 최단 거리 갱신
                heapq.heappush(q, (cost, i[0])) # 갱신된 정보를 새로 큐에 삽입 => 연결된 모든 애들 중 원래 테이블 보다 짧은 거만 갱신!!

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
import sys
import heapq
input = sys.stdin.readline

# 전보를 받는 도시 수 & 총 시간

n, m, city = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1) # 최단 거리 테이블 필요

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # 다익스트라 그래프는 (도착점, 거리) 형식으로 담음

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # list, (distance, node)
    distance[start] = 0 # 자기 자신과의 거리는 0
    
    while q:
        dist, now = heapq.heappop(q) # 힙에는 (거리, 노드) 순으로 담음. 정렬 때문에
        
        if distance[now] < dist: # 이미 처리한 노드라면 무시 (그림에서 뽑은 놈이 테이블에 밀리는 case)
            continue
        
        for j in graph[now]: # j는 (end, dist) 튜플. 연결된 애들을 하나씩 확인
            cost = dist + j[1] # now 노드를 거쳐서 j의 end로 가는 비용
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0])) # 갱신된 거리랑 end 노드를 다시 넣어줌

dijkstra(city)

cnt = 0 # 도달 할 수 있는 도시의 개수

max_diatance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_diatance = max(max_diatance, d)

print(cnt - 1, max_diatance) # 시작 노드는 제외해야 해서 - 1
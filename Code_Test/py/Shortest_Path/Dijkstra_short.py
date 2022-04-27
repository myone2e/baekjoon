import sys
input = sys.stdin.readline
INF = int(1e9)
# Dijkstra: 인접 리스트를 이용하는 방식. 노드 갯수 만큼 리스트를 만들어 각 노드와 연결된 모든 간선에 대한 모든 정보를 리스트에 저장

n, m = map(int, input().split()) # num vertices, num edges
start = int(input())

graph = [[] for i in range(n+1)] # +1 for indexing (vertex starts at 1) 
visited = [False] * (n+1)
distance = [INF] * (n+1) # shortest distance table

# receive edges
for _ in range(m):
    a, b, c = map(int, input().split()) # from a to b , distance is c 
    graph[a].append((b,c)) # distance may vary between two nodes!
    
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # just initialize
    for i in range(1, n+1): # 선형탐색 부분 ! 이걸 heapq로 대체해야함
        if distance[i] < min_value and not visited[i]: # 방문 안한 애들만
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # 연결된 노드에 대해 (노드 번호, 거리로 들어있음)
        distance[j[0]] = j[1] # 노드번호, 거리
        
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for _ in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서
        now = get_smallest_node()
        visited[now] = True # 방문 처리
        
        for j in graph[now]: # 선택된 노드와 연결된 애들
            cost = distance[now] + j[1] # 거리 더하고
            
            if cost < distance[j[0]]: # 바로 가는거보다 짧다면
                distance[j[0]] = cost # 최단 거리 갱신

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
        

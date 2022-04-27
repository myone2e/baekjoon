from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1) # 문제가 1번 노드부터 시작함으로
graph = [[] for _ in range(v+1)] # 거리가 없으므로 연결 리스트

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # A에서 B로 이동 가능
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0: # 진입차수 0인 애들
            q.append(i) # 노드 번호를 큐에 넣음
    
    while q:
        now = q.popleft()
        result.append(now) # 결과에 이어 붙이기
        
        for i in graph[now]: # 해당 노드와 연결되 간선 제거 = 연결된 노드들의 진입차수 1 빼기
            indegree[i] -= 1
            if indegree[i] == 0: # 빼서 0이 됐으면 새로 큐에 삽입
                q.append(i) # 이 과정에서 여러개가 들어간다면 답이 여러개 존재!!

    for i in result:
        print(i, end = ' ')
    print()
topology_sort()
        
        
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 첫 노드를 큐에 삽입
    visited[start] = True # 현재(첫) 노드를 방문 처리
    
    #큐가 빌 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결되고 아직 방문하지 않은 원소를 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], # 첫 칸을 비워놓고 노드 번호대로 가도록!
    [2, 3, 8], # 노드 1이 2, 3, 8과 연결되어 있다
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [0] * 9

bfs(graph, 1, visited) # v 가 순서대로 출력됨!
print()
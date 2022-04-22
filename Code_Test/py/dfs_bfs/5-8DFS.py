def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # 1번 노드 => 2, 3, 8
        if not visited[i]:
            dfs(graph, i, visited) ## i가 다시 v로 들어가는 구조!

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

visited = [0] * 9 # 각 노드가 방문된 정보(순서)를 리스트로 저장

dfs(graph, 1, visited) # v = 1 : 1번에서 출발하겠다
print()
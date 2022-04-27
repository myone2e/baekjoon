import sys
input = sys.stdin.readline

def find_parent(parent, x): # parent는 부모 노드를 기록한 리스트
    if parent[x] != x: # 자기 자신이 부모가 아니라면 = 루트 노드가 아니라면
        return find_parent(parent, parent[x]) # 하나 올라가서 다시 찾기
    return parent[x] # 해당 노드의 루트 노드가 바로 부모 노드가 되도록 => 시간 단축

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # big이 small을 가르키게
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
edges = [] # 모든 간선을 담을 리스트! 최소 신장 트리는 그래프 아님
result = 0 # 비용

parent = [0]*(v+1)
for i in range(v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))  # 비용 순으로 정렬하기 위해 cost를 맨 앞에 설정

edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간산 중에서 가장 비용이 큰 간선을 저장하기 위함

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge # tuple 풀기
    # 사이클이 발생하지 않는 경우만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        last = max(last, cost)
        result += cost

print(result - last)
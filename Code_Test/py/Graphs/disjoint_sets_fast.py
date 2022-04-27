# 특정 원소가 속한 집합을 찾기

# O(V + M*(1 + log...))
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
parent = [0] * (v+1)

# 자기 자신으로 부모를 초기화
for i in range(1, v+1):
    parent[i] = i 

# input에 따라 union 연산을 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a,b)
    
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end ='')
for i in range(1, v+1):
    print(parent[i], end = ' ')
print()
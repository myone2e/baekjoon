import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [0] * (n+1) # 학생 번호가 1로 시작해서 + 1

for i in range(0, n+1): # 부모를 자기 자신으로 초기화
    parent[i] = i

for i in range(m): # command 받는 횟수
    cmd, a, b = map(int, input().split())
    
    if cmd == 0: # 팀을 합치는 연산인 경우
        union_parent(parent, a, b)
    elif cmd == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
import sys
from collections import deque
import copy

input = sys.stdin.readline

v = int(input())
indegree = [0] * (v+1) # 문제가 1번 노드부터 시작함으로
graph = [[] for _ in range(v+1)] # 거리가 없으므로 연결 리스트
result = [0]*(v+1)

time = [0] * (v+1) # time table 따로 빼기

for i in range(1,v+1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    ptr = 1
    while line[ptr] != -1:
        graph[i].append(line[ptr])
        indegree[line[ptr]] += 1
        ptr += 1

def topology_search(start):
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v+1):
        print(result[i])

topology_search()
    



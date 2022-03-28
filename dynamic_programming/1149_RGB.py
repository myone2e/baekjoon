import sys
input = sys.stdin.readline

N = int(input())

d = [0]

for _ in range(1, N+1):
    d.append(list(map(int, input().split())))
    
for i in range(2, N+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][1], d[i-1][0]) + d[i][2]

print(min(d[N]))
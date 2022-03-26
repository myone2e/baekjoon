import sys
input = sys.stdin.readline

N = int(input())

d = [0] * (N+1)
stair = [0] # index 맞추기 위해서
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])

else:
    d[1] = stair[1]
    d[2] = stair[1] + stair[2] 
    for i in range(3, N+1):
        d[i] = max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])  # 연속 or not
    print(d[N])
import sys
input = sys.stdin.readline
n = int(input()) # N x 2 table

d = [0] * (n+1)

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    # 세로로 긴거 + 큰거 + 가로 두개 => 세로로 긴거에서 카운트해서 세로 두개는 제외
    d[i] = (d[i-1] + d[i-2] + d[i-2]) % 796796 

print(d[n])
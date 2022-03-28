import sys
input = sys.stdin.readline

INF = 1e9

c, n = map(int, input().split())
d = []

dp = [INF] * (c+100) # initiate table with large numbers # + 100 to check answers beyond 
dp[0] = 0

for _ in range(n):
    # cost, customer
    d.append(list(map(int, input().split())))

# cost ascending order
d_sort = sorted(d, key = lambda x: x[0])

# dp[ num ] = min ( dp[ num - cus ] + cost , dp[ num ] ) 
for cost, cus in d_sort:
    for i in range(cus, c+100):
        dp[i] = min(dp[i-cus] + cost, dp[i])

print(min(dp[c:]))


n = int(input())

lst = list(map(int, input().split()))

d = [0] * 100

# Bottom up DP
d[0] = lst[0]
d[1] = max(lst[0], 0 + lst[1]) # 점화식 적용
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + lst[i])

print(d[n-1]) 
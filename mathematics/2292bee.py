N = int(input())

start = 1

cnt = 0
i = 1
while start < N: #등호 없어야 함. 걔 까지도 카운트
    cnt += 1
    start += 6*i
    i += 1
print(cnt + 1)
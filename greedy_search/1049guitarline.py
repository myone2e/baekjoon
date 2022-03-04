from math import remainder


N, M = map(int, input().split())
# package = 6
# N: my demand
# M: number of options
total_money = 0
packages = []
indiv = []
for _ in range(M):
    pack, ind = map(int, input().split())
    packages.append(pack)
    indiv.append(ind)
packages.sort()
indiv.sort()

if packages[0] > 6 * indiv[0]: # 낱개가 더 싼 경우
    result = indiv[0]*N
else: 
    r = N % 6  # 남는 수량
    if packages[0] < r*indiv[0]: # 낱개 추가가 비싼 경우
        if r:
            result = packages[0] * (N//6 + 1)
        else:
            result = packages[0] * (N//6) # 나머지가 없는 경우 초과 안되도록
    else:
        result = packages[0] * (N//6) + r*indiv[0]

print(result)
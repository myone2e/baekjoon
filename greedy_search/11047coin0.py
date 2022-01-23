N, K = map(int, input().split())
cand = []
for _ in range(N):
    cand.append(int(input()))
    
cand.sort()

total = 0
for i in cand[::-1]:
    if i == 1:
        total += K
        break
        
    elif K // i:
        total += K // i
        K -= K // i * i #이게 중요 했음. //i * i 개념 인지
    else:
        pass
print(total)
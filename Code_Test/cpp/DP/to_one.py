x = int(input())

d = [0] * 30000

# bottom-up dp
for i in range(2, x+1): # 1은 1로 만들 필요가 없으므로
    d[i] = d[i-1] + 1 # +1은 한번 더 연산했다
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])

P = int(input())
L = 1000 - P

cand = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in cand:
    while L >= i:
        L -= i
        cnt += 1
print(cnt)
T = int(input()) #in seconds
cand = [300, 60, 10]
counter = []

if T % 10 != 0:
    print(-1)
else:
    for t in cand:
        cnt = 0
        while T >= t:
            T -= t
            cnt += 1
        counter.append(cnt)
for c in counter:
    print(c, end= ' ')
print()
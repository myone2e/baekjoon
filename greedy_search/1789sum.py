S = int(input())
#S = sum of N natural numbers
cand = [n*(n+1)/2 for n in range(1,100000)]
cnt = 0
for num in cand:
    if S >= num:
        cnt += 1
    else:
        break
print(cnt)
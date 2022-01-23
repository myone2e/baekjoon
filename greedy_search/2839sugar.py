N = int(input())
#51퍼에서 틀렸습니다.
mod5 = N//5

list5 = [i*5 for i in range(1,mod5+1)]
cand = []
for i in list5:
    if (N - i)%3 == 0:
        cand.append((N-i)//3 + i//5)
if cand ==[]:
    print(-1)
elif N//3 < min(cand):
    print(N//3)
else:
    print(min(cand))


    
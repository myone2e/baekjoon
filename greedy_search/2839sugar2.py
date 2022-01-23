N = int(input())

def sugar(N):
    if N%5 == 0:
        return int(N/5)
    
    mod5 = N//5

    list5 = [i * 5 for i in range(1,mod5+1)]
    cand = []
    for i in list5:
        if (N - i)%3 == 0:
            cand.append(i/5 + (N-i)/3)
    if cand == []:
        if N%3 == 0: #6, 9 등을 놓쳐서 에러 발생한 케이스
            return int(N/3)
        else:
            return -1
    else:
        return int(min(cand))

print(sugar(N))
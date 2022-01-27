N = int(input())
for _ in range(N):
    result = input()
    score = 0
    cnt = 0
    for s in result:
        if s =='O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
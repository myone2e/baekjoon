T = int(input()) #테스트 횟수
for _ in range(T):
    N = int(input()) #한 테스트 당 지원자 수
    nest = []
    
    for _ in range(N):
        nest.append(list(map(int, input().split())))
    nest.sort()
    
    max = nest[0][1] #서류 기준 오름차순 정렬 => 순위임! => 서류 1등은 무조건 선발
    
    cnt = 1
    for i in range(1,N):
        if max > nest[i][1]:
            cnt += 1
            max = nest[i][1]
    print(cnt)
    
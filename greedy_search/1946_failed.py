T = int(input()) #테스트 횟수
for _ in range(T):
    N = int(input()) #한 테스트 당 지원자 수
    
    cnt = N
    A, B = map(int, input().split()) #맨 앞에를 세운다 => 얘가 죽이는 애가 죽이는 애를 놓침 => 이게 아니라 점수가 아니라 순위엿음!
    for _ in range(1, N):
        a, b = map(int, input().split())
        if A > a and B > b:
            cnt -=1
        elif A < a and B < b:
            cnt -=1
            A = a ; B = b
        else:
            continue
    
    print(cnt)
#결과적으로 실패
        
        


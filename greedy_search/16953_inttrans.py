A, B = map(int, input().split()) #A <= B 조건 주어짐
cnt = 1

while A != B:
    
    if A > B:
        break
    
    elif B % 10 == 1:
        B = (B - 1) / 10
        cnt += 1
    else: #***elif만 else로 바꿔도 시간 단축 유의미
        B = B / 2
        cnt += 1
    
if A != B:
    print(-1)
else:
    print(cnt)




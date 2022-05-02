import sys
input = sys.stdin.readline

s = input().strip()

def flip_string(s):
    start = s[0]
    cnt0, cnt1 = 0, 0 # 전부 0으로 바꾸는 경우 & 전부 1로 바꾸는 경우
    
    if s[0] == '1': # 전부 0으로 바꾸는 경우 시작부터 +1
        cnt0 += 1
    else:
        cnt1 += 1
    
    for i in range(len(s)-1): # 두 번째 원소부터 확인
        if s[i] != s[i+1]: # 바뀌는 지점
            if s[i+1] == '1': # 0에서 1로 바뀐다
                cnt0 += 1 # 최소 1 번은 더 뒤집어야 함
            else:
                cnt1 += 1
    
    return min(cnt0, cnt1)
print(flip_string(s))
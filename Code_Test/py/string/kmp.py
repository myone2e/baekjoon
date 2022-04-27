import sys
input = sys.stdin.readline

def kmp_match(txt, pat):
    
    pt = 1 # 이걸 위의 패턴의 포인터로 사용
    pp = 0
    skip = [0] * (len(pat) + 1)
    
    skip[pt] = 0 
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] == pp
        else:
            pp = skip[pp]
            
    pt = 0; pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
            
    return pt - pp if pp == len(pat) else -1

s1 = input().rstrip() # 이거 안해주면 인식이 안된다
s2 = input().rstrip()

idx = kmp_match(s1, s2)
if idx == -1:
    print('None')
else:
    print(idx + 1)
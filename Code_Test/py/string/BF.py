import sys
input = sys.stdin.readline
# 패턴이 txt안에 존재하는지 탐색. 존재하면 index 반환
# O(nm) n: len(txt), m: len(pat)
def bf_match(txt, pat): # txt pattern
    pt = 0 # pointer text
    pp = 0
    
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else: # 다르면 pattern은 처음부터 & txt는 같기 시작했던 다음 칸으로
            pt = pt - pp + 1 # 이걸 그냥 그림으로 pat를 한 칸 밀어서 다시 비교를 시작한다고 생각
            pp = 0 # 얘는 항상 처믐부터 비교해야 하니까
    return pt - pp if pp == len(pat) else -1

s1 = input().rstrip() # 이거 안해주면 인식이 안된다
s2 = input().rstrip()

idx = bf_match(s1, s2)

if idx == -1:
    print('None')
else:
    print(idx + 1)
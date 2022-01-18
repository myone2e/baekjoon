import sys

A, B, C = map(int, sys.stdin.readline().split()) #fc, vc, p

#while True 하면 시간 초과 (범위가 21억)
if B >= C:
    print('-1')
else:
    n = A // (C - B) #fc가 커버가 되는가
    print(n+1)

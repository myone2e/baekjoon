import sys
A, B = map(int, sys.stdin.readline().split())
if A > B: #B가 더 크게
    A, B = B, A

result = 0
result = (A + B) * (B - A + 1) / 2
print(int(result))
    
                      
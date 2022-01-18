import sys
A, B = map(int, sys.stdin.readline().split())
if A > B: #B가 더 크게
    A, B = B, A

result = 0
if A < 0 and B > 0:
    temp = B - abs(A)
    for i in range(temp, B+1):
        result += i
elif A > 0 and B > 0:
    for j in range(B-A, B+1):
        result += j
else:
    for k in range(A, B+1):
        result += k
print(result)

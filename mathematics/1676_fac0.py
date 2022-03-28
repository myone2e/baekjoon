import sys
input = sys.stdin.readline
import math

n = int(input())
s = list(str(math.factorial(n)))

cnt = 0
for num in reversed(s):
    if num == '0':
        cnt += 1
    else:
        break
print(cnt)
# Top down (by recursion = call small to solve big problem)
import sys
input = sys.stdin.readline
n = int(input())
d = [0] * (n+1) # Memoization != DP table
# Memoization is cache => Don't have to use it for DP

def fibo(x):
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0: # 이미 풀었던 문제는 풀어도 되지 않게
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    
    return d[x]

print(fibo(n))
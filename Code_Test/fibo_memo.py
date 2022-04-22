# Top down (by recursion = call small to solve big problem)
import sys
input = sys.stdin.readline
n = int(input())
def fibo(x):
    d = [0] * (x+1) # Memoization

    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0: # don't have to solve problems again
        return d[x] 
    
    d[x] = fibo(x-1) + fibo(x-2)
    
    return d[x]

print(fibo(n))
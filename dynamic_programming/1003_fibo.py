import sys
input = sys.stdin.readline

N = int(input())
 
for _ in range(N):
    a = [1,0] # count zero
    b = [0,1] # count one
    n = int(input())
    if n>1:
        for i in range(n-1):
            a.append(b[-1])
            b.append(a[-2]+b[-1]) 
 
    print(a[n], b[n])
    

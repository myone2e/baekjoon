import sys
input = sys.stdin.readline
n = int(input())

d = [0] * (n+1)
# ai = min(ai-1, ai/2, ai/3, ai/5) + 1

# all if => check all cases ex) 30
for i in range(2, n+1):
    d[i] = d[i] + 1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
        
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
        
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
        
print(d[n])
    
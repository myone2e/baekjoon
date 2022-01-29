N, K = map(int,input().split())

comb = 1
for i in range(N, N-K, -1):
    comb *= i
for j in range(K, 1, -1):
    comb /= j 
    
print(int(comb))
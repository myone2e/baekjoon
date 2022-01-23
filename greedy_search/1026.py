N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
B = B[::-1]
treasure = 0
for i in range(N):
    treasure += A[i]*B[i]
    
print(treasure)

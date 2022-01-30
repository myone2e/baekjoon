N = int(input())

for i in range(1, N):
    n = i
    for j in str(i):
        n += int(j)
    if n == N:
        const = i
        break

try:
    print(const)
except:
    print(0)
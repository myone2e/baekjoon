N = int(input())
lst = []
for _ in range(N):
    n = int(input())
    lst.append(n)
lst.sort()
for i in lst:
    print(i)


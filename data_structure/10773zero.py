N = int(input())
lst = []

for _ in range(N):
    n = int(input())
    if n == 0:
        lst.pop(-1)
    else:
        lst.append(n)
print(sum(lst))
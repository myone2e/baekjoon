import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = [input().strip() for i in range(N)] # strip 사용해야 띄어쓰기 없이 잘 들어감
see = [input().strip() for j in range(M)]

dup = sorted(list(set(listen) & set(see)))

print(len(dup))

for i in dup:
    print(i)
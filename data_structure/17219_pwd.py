import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = {}

for _ in range(N):
    url, pwd = input().split()
    d[url] = pwd

for _ in range(M):
    req = input().rstrip()
    print(d[req])
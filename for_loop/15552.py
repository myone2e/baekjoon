import sys

#input()을 사용하면 시간 초과

N = int(sys.stdin.readline())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
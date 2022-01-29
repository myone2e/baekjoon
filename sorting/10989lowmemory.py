import sys
# append보다 적은 메모리 사용

N = int(sys.stdin.readline())
lst = [0] * 10001 # 자연수 10000개

for _ in range(N):
    lst[int(sys.stdin.readline())] += 1 

for i in range(1,10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)
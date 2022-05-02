import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 공의 갯수, 공의 최대 무게

balls = list(map(int, input().split()))

array = [0] * 11 # 1부터 m까지의 무게를 담는 리스트

for b in balls:
    array[b] += 1

result = 0
for i in range(1, m+1):
    n -= array[i] # 같은 무게 못 고르니 제외 # 왜 마이너스 계속 가지고 가는지는 모르겟따
    result += array[i] * n

print(result)
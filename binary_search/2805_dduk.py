import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0 
    mid = (start + end) // 2
    for x in arr: # x = 떡의 길이
        if x > mid: # 절단기보다 크면 짤린다
            total += x - mid # 떡 짤린 합
    if total < M: # 부족하다면 절단기를 줄인다
        end = mid - 1
    else:
        result = mid
        start = mid + 1 # 여기서 while 가서 end 만난다면, 이전 값 리턴
print(result)


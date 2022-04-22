array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start ,end):
    if start >= end: # 원소가 1 개인 경우 종료
        return
    
    pivot = start # 첫 원소가 기준
    left = start + 1 # 왼쪽에서 오른쪽으로 가면서 start보다 큰 애 찾음
    right = end # 오른쪽에서 왼쪽으로 가면서 start보다 작은 애 찾음
    
    while left <= right: 
        while left <= end and array[left] <= array[pivot]: # 오른쪽 끝까지 가기 전이고 pivot보다 작다면 큰 데이터를 찾기 전까지 반복
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # cross 되었다면 작은 데이터와 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[pivot] = array[pivot], array[left]
    
    quick_sort(array, start, right - 1) # 왼쪽을 정렬
    quick_sort(array, right+1, end)  # 오른쪽을 정렬

quick_sort(array, 0, len(array)-1)
print(array)
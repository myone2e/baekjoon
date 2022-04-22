def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 버림
    
    if array[mid] == target:
        return mid
     
    elif array[mid] > target: # 왼쪽에 있다면 mid -1 을 새로운 끝점으로
        return binary_search(array, target, start, mid-1)
    
    else: # 오른쪽에 있다면 mid + 1을 새로운 시작점으로
        return binary_search(array, target, mid+1, end)
    
# 몇 번째냐 물어보면 리턴 값 + 1

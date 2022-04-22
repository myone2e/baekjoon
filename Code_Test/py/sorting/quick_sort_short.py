from turtle import right


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_short(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    return quick_short(left_side) + [pivot] + quick_short(right_side) # list 이렇게 잇기도 가능!

print(quick_short(array))
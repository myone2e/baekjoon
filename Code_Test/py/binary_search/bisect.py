from bisect import bisect_left, bisect_right
# 정렬된 리스트에만 사용 
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a,x)) # 데이터를 삽입할 가장 왼쪽 인덱스 찾아줌 2
print(bisect_right(a,x)) # 데이터를 삽입할 가장 오른쪽 인덱스 찾아줌 4

b = [1,2,3,4,5,6,7,8,9]
y = 5
print(bisect_left(b,y)) # 4
print(bisect_left(b,y)) # 4


def count_by_range(a, l, r):
    right_idx = bisect_right(a, r)
    left_idx = bisect_left(a, l)
    return right_idx - left_idx

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, 4, 4)) # 값이 4인 데이터의 갯수 출력 2
print(count_by_range(a, -1, 3)) # 값이 -1 과 3 사이인 데이터의 갯수 출력 6
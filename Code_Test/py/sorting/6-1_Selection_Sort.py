array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 서치 전에 초기화.  뒤에 원소 j 시작점으로 이용하기 위해서
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: # 뒤에서 최소를 찾는 것
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
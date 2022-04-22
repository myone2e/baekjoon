array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# j 앞 부분은 이미 정렬 되어 있음이 전제 => 거꾸로 돌면서 큰 애부터 비교
for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 지금 돌고 있는 애가 더 작다면
            array[j] , array[j-1] = array[j-1], array[j]
            
        else: # 앞쪽에 더 작은 애를 만나면 거기서 멈춰라
            break;
print(array)
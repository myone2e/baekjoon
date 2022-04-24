import heapq

def heapsort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, -value) # list, item # 부호 바꿔서 넣고
        
        for _ in range(len(h)):
            result.append(-heapq.heappop(h)) # pop from min value # 꺼내서 다시 바꿔주고
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
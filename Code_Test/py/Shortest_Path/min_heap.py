import heapq

def heapsort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, value) # list, item
        
        for _ in range(len(h)):
            result.append(heapq.heappop(h)) # pop from min value
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
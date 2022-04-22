import sys
input = sys.stdin.readline
N = int(input())
inv = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))
inv.sort()

def binary_search(array, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1 
        else:
            start = mid + 1
    return None

for t in order:
    result = binary_search(inv, t, 0, N-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
print()
    
cnt = 0
lst = []
def hanoi(num, x, y, support):
    global cnt, lst
    if num == 1:
        lst.append([x,y])
        cnt += 1
        return
    hanoi(num-1, x, support, y)
    lst.append([x,y])
    cnt += 1
    hanoi(num-1, support, y, x)
    return cnt, lst
N = int(input())
result = hanoi(N, 1, 3, 6-3-1)
if N != 1:
    print(result[0])
    for pair in result[1]:
        print(pair[0], pair[1])
if N == 1:
    print(1)
    print(1, 3)

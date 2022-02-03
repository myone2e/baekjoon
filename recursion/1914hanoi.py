#cnt = 0
lst = []
def hanoi(num, x, y, support):
    global lst, N # global cnt => 답을 모르는 경우에 사용
    if num == 1:
        if N <= 20:
            lst.append([x,y])
        #cnt += 1
        return
    hanoi(num-1, x, support, y)
    if N <= 20:
        lst.append([x,y])
    #cnt += 1
    hanoi(num-1, support, y, x)
    return lst
N = int(input())
if N > 20:
    print(2**(N)-1) # 항상 2^n - 1번!
else:
    print(2**(N)-1)
    result = hanoi(N, 1, 3, 2)
    for pair in result:
        print(*pair)

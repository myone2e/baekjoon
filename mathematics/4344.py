N = int(input())
for _ in range(N):
    obj = map(int, input().split()) #temporal object
    lst = list(obj) #to list
    avg = sum(lst[1:]) / lst[0]
    cnt = 0
    for i in lst[1:]:
        if i > avg:
            cnt += 1
    ratio = cnt / lst[0] * 100
    print('{:.3f}%'.format(ratio))
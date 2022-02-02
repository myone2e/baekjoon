N = int(input())
for _ in range(N):
    lst = list(input())
    cnt = 0
    for p in lst:
        if p == '(':
            cnt += 1
        elif p == ')':
            cnt -= 1
        if cnt < 0:
            break;
    if cnt == 0:
        print("YES")
    else:
        print("NO")

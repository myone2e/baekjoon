N, K = map(int, input().split())

lst = [n for n in range(1, N+1)]
print('<', end ='')
step = 0
while True:
    step += K - 1 # 지워지는 애 인덱스 때문에 -1
    if step >= len(lst):
        step = step%len(lst) # ex) step = 6 & len = 5(마지막 인덱스 4) => 1로
    if len(lst) == 1:
        break
    p = lst.pop(step)
    print(f'{p},', end = ' ')
print(f'{lst[0]}>')


        
    
     

# <3, 6, 2, 7, 5, 1, 4>
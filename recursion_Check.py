def spread_virus():
    print('condition set!')

    
def build_wall(cnt): # 나중에 0을 넣어서 시작
    if cnt == 3:
        spread_virus()
        return
    print(f'cnt: {cnt}')
    build_wall(cnt+1)
    print(f'return the wall {cnt}')

build_wall(0)


# cnt: 0
# cnt: 1
# cnt: 2
# condition set!
# return the wall 2
# return the wall 1
# return the wall 0
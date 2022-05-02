import sys
input = sys.stdin.readline

n = int(input())

coins = list(map(int, input().split()))
coins.sort()

def getImpossible(coins):
    target = 1
    # target - 1까지는 다 만들 수 있다고 본다
    for c in coins: 
        if target < c: # 1, 1, 1, 5 를 예시로 들면 4 까지 증가시키고 5가 크니까 4 리턴
            break
        
        target += c
        
    return target

print(getImpossible(coins))
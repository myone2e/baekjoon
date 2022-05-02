import sys
input = sys.stdin.readline

n = int(input())
fears = list(map(int, input().split()))
fears.sort()

def getMaxGroup(fears):
    cnt = 0
    num_members = 0
    
    for k in fears:
        num_members += 1
        if num_members >= k:
            cnt += 1
            num_members = 0
    return cnt
print(getMaxGroup(fears))
    
    
    
        
        
    
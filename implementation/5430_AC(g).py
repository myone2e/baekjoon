import sys
from collections import deque
input = sys.stdin.readline

# deque.reverse() 많이 쓰면 시간 초과 => reverse counting해서 짝수면 popleft 홀수면 pop

T = int(input())

for _ in range(T):  
    commands = input() 
    n = int(input()) 
    arr = deque(input().rstrip()[1:-1].split(",")) # rstrip for \n

    if n == 0:
        arr = deque()
        
    errFlag = 0
    directionFlag = 0 # no reverse

    for c in commands:
        if c == "R":
            if directionFlag == 0:
                directionFlag = 1
            elif directionFlag == 1:
                directionFlag = 0
        elif c == "D":
            if len(arr) == 0 :
                print("error")
                errFlag = 1
                break;

            if directionFlag == 0:
                arr.popleft()
            elif directionFlag == 1:
                arr.pop()
      
    if commands.count('R') % 2: # reverse 홀수면
        arr.reverse()
        
    if errFlag==0:
        print("["+",".join(arr)+"]")
    
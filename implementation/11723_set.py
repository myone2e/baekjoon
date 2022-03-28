import sys
input = sys.stdin.readline

N = int(input())
S = set()

# input 길이가 일정하지 않을 경우 len으로 처리!
for _ in range(N):
    tmp = input().strip().split()
   
    if len(tmp) == 1:
        if tmp[0] == "all":
            S = set([n for n in range(1, 21)])
        else:
            S = set()  
    else:
        command, num = tmp[0], tmp[1]
        num = int(num)

        if command == "add":
            S.add(num)
        elif command == "remove":
            S.discard(num)
        elif command == "check":
            print(1 if num in S else 0)
        elif command == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)

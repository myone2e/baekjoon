import sys

# Queue 는 insert로 앞에서부터 박아 넣어야 함! => 이러면 rear, front 필요 없음!
que = []
N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().split()
    c = command[0]
    if c == 'push':
        que.insert(0, int(command[1]))
        
    elif c == 'pop':
        if len(que) > 0:
            p = que.pop()
            print(p)
        else:
            print(-1)
    elif c == 'size':
        print(len(que))
    elif c == 'empty':
        if len(que) > 0:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)
    elif c == 'back':
        if len(que) > 0:
            print(que[0]) # rear는 들어올 자리!
        else:
            print(-1)
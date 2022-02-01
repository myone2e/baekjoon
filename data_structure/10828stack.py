import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    command = sys.stdin.readline().split()
    c = command[0]
    if c == 'push':
        stack.append(int(command[1]))
    
    elif c =='pop':
        if len(stack) > 0:
            p = stack.pop(-1)
            print(p)
        else:
            print(-1)

    elif c == 'size':
        print(len(stack))
        
    elif c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c =='top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
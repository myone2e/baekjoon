from collections import deque
from turtle import left # 가장 앞에 삽입 삭제 하는데 O(1) vs list는 O(N)
# FIFO (like the lines of CAVA)
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # delete the first element # appendleft 하면 가장 앞에 원소 삽입 가능

queue.append(1)
queue.append(4)
queue.popleft() # delete the first element
queue.pop() # delete the last(recent) element
queue.appendleft(9) # insert 9 at the first

print(queue)
queue.reverse()
print(queue)

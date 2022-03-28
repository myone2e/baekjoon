# First in First out (stack on the top)
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # delete 7
stack.append(1)
stack.append(4)
stack.pop() # delete 4

print(stack)
print(stack[::-1])
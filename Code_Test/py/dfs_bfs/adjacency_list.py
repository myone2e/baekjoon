# use less memory, but slow
graph = [[] for _ in range(3)] # [ [], [], []]

graph[0].append((1,7)) # from 0 to 1 with len 7
graph[0].append((2,5)) # from 0 to 2 with len 5

graph[1].append((0,7)) # from 1 to 0 with len 7

graph[2].append((0,5)) # from 2 to 0 with len 5

print(graph)
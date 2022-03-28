INF = 1e9 # not connected

# using two-dim list
graph = [
    [0, 7, 5], # number = len(edge)
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# use memory more, but fast
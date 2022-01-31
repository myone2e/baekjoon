cand = []
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    cand.append(i)
    
    
    
for j in range(1, 10001):
    if j not in cand:
        print(j)
    else:
        continue
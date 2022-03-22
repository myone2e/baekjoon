# Top down (by recursion = call small to solve big problem)
d = [0] * 100 # Memoization

def fibo(x):
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0: # 이미 풀었던 문제는 풀어도 되지 않게
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    
    return d[x]

print(fibo(6))
N = int(input())

def check_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int((n**0.5))+1):
            if n % i == 0:
                return False
    return True
    
lst = map(int, input().split())
cnt = 0
for num in lst:
    if check_prime(num):
        cnt += 1
print(cnt)
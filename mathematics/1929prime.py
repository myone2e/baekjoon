M, N = map(int, input().split())

def check_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1): #제곱근 까지만 확인 
            if n%i == 0:
                return False
        return True

for i in range(M, N+1):
    if check_prime(i):
        print(i)

#TF return하는 함수 사용하는 것은 매우 좋은 방법 => 나중에 관련 문제에서 다시 활용 가능

#n = a * b

#16 = 1 * 16

#16 = 2 * 8

#16 = 3 * (어떤 복잡한 수)

#16 = 4 * 4

#16 = 5 * (어떤 복잡한 수이나, 4보다는 작은수)

#16 = 8 * 2

#16 = 16 * 1 이 된다.
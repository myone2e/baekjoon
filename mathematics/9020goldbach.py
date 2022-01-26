N = int(input())

def check_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1): #제곱근 까지만 확인 
            if n%i == 0:
                return False
        return True

for _ in range(N):
    num = int(input())
    lb = num / 2
    rb = num / 2 
    while True:
        if check_prime(lb) and check_prime(rb):
            print(int(lb), int(rb))
            break
        else:
            lb -= 1
            rb += 1
    
            
        
    
    
    

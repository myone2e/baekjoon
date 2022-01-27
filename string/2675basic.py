N = int(input())
for _ in range(N):
    n, QR = input().split()
    string = ''
    for i in QR: #str 도 iterable하다
        string += i * int(n)
    print(string)
    

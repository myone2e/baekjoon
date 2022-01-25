N = list(input())
N.sort(reverse=True) #str list sorting 가능 => 최대를 뽑기 위해 역순으로 sorting

#30의 배수가 되려면 각 자리의 숫자를 더했을 때 3의 배수여야 함!
sum = 0
for n in N:
    sum += int(n)

if sum % 3 != 0 or '0' not in N:
    print(-1)

else:
    print(('').join(N)) #str 이어붙이기 #'-'.join(N) 이면 2-1-0
    #join은 중간에 끼어넣는다.
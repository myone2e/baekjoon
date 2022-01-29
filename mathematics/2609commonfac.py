A, B = map(int, input().split())

# A가 작게 정렬
if A > B:
    A, B = B, A
 
# greatest common divisor
def gcd(A, B):
    mcf = 0 
    for n in range(1, A+1):
        if A % n == 0 and B % n == 0:
            mcf = n
    return mcf

# least common multiple = abs(A*B) / gcd(A,B)
def lcm(A, B):
    least = abs(A*B) / gcd(A, B)
    return int(least)

print(gcd(A,B))
print(lcm(A,B))
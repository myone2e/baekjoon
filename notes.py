import sys
input=sys.stdin.readline

def merge(C,D):
    global cnt
    lc, ld = len(C), len(D)
    i, j = 0, 0
    B = []
    while i < lc and j < ld:
        if C[i] < D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            j += 1
            cnt += lc - i
    if i == lc:
        B.extend(D[j:])
    elif j == ld:
        B.extend(C[i:])
    
    return B
                

def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = (len(A) - 1) // 2 # len(A) 쓰면 recursion error
    C = merge_sort(A[:mid+1])
    D = merge_sort(A[mid+1:])
    
    return merge(C, D)

N = int(input())
cnt = 0
lst = list(map(int, input().split()))
merge_sort(lst)
print(cnt)
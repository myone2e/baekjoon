import sys
input = sys.stdin.readline

# Stanford Algorithms week2 

def merge_and_countsplitinv(C, D): # sorted Arrays
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
                
# Recursively call merge
def merge_and_countinv(A):
    if len(A) <= 1:
        return A
    nby2 = int((len(A)) // 2)
    C = merge_and_countinv(A[:nby2])
    D = merge_and_countinv(A[nby2:])
    
    return merge_and_countsplitinv(C, D)

N = int(input())
cnt = 0
lst = list(map(int,input().split()))
merge_and_countinv(lst)
print(cnt)
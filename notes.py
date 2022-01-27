word = input().upper()

S = set(list(word)) # alphabet 하나씩만
S = list(S)

lst = []
for w in S:
    cnt = 0
    for a in word:
        if a == w:
            cnt += 1
    lst.append(cnt)
    
max = max(lst) #가장 많이 나온 횟수
idx = lst.index(max)
del lst[lst.index(max)]
if max in lst:
    print('?')
else:
    print(S[idx])

# 집합은 indexing slicing 불가 => set 후 다시 list 만들어야 접근 가능

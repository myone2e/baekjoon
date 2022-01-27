N = int(input())

S = set()
for _ in range(N):
    S.add(input())
lst = list(S)
lst.sort() # 알파벳 순으로
lst.sort(key = lambda x: len(x)) # 길이 순으로
for w in lst:
    print(w)
word = input().upper()
word.sort()
S = set(list(word)) # alphabet 하나씩만

lst = []
for w in S:
    cnt = 0
    for a in word:
        if a == w:
            cnt += 1
        lst.append(cnt)
max = max(lst)
print(max)
        
        


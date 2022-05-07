s = list(input())

mid = int(len(s)/2) 

first = s[:mid]
second = s[mid:]

f, s = 0, 0
for i in first:
    f += int(i)
    
for j in second:
    s += int(j)
    
if f == s:
    print('LUCKY')
else:
    print('READY')

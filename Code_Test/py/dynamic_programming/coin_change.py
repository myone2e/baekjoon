import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
for _ in range(len(arr)):
    arr.append(int(input()))

d = [1e9] * (m+1) # fill with big numbers

d[0] = 0 # 0 by 0 coins
for i in range(n): # looping the coins
    for j in range(arr[i], m+1): # money larger than coin
        if d[j - arr[i]] != 1e9: # if there is a way to make j - k won => we can move on by adding k 
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 1e9:
    print(-1)

else:
    print(d[m])

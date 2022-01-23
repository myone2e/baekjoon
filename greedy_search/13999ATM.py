n = int(input())
obj = map(int, input().split()) #temporal object
lst = list(obj)
lst.sort() #to get minimum
wait = 0
total = 0
for i in lst:
    wait += i
    total += wait
print(total)
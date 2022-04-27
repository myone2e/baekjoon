s = 'https://github.com/myone2e?tab=repositories'

print(s.find('github')) # return first index
print(s.find('t'))
print(s.find('github', 5, 13)) # from idx [5 to 13)

print(s.rfind('s')) # 오른쪽에서부터 처음 나오는 index

print(s.index('github')) # find와 동일하지만 없으면 ValueError


# 아래도 [start, end) 지정 가능
print(s.startswith('https:')) 
print(s.startswith('https:', 5)) 

print(s.endswith('https'))
print(s.endswith('repositories'))

def add_1(n):
      return n + 1

target = [1, 2, 3, 4, 5]

result = map(add_1, target) # result = map(lambda x : x+1, target) 와 동일

print(list(result))

# filter: 함수가 참이면 해당 데이터를 반환
# filter(function, data) => 데이터의 값이 차례대로 x로 함수에 들어가고 참이면 그 데이터를 반환
string = '0001100'
res = list(filter(lambda x: string[x]=='0', range(len(string)))) # string의 n 번째가 0이라면 n을 반환
print(res)

string = '0001100'
res = list(filter(lambda x: x=='0', string)) # 여기는 string에 한 원소씩 0과 비교하고 0이면 그 원소(0)을 반환
print(res)

target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x : x%2==0, target)
print(list(result))
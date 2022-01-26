N = int(input())

alpha_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0,
              'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0,
              'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0,
              'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alpha_list = []
words = []


for _ in range(N): #AAA, AABC 등 input의 list를 생성
    word = list(input())
    words.append(word)

for word in words: #100의자리 1번 10의 자리 1번이면 value가 110 되게 끔 설정
    for i in range(len(word)):
        num = 10**(len(word) - 1 - i) 
        alpha_dict[word[i]] += num

for v in alpha_dict.values(): #10000, 1010, 1000, 110 등 전부 추가
    if v > 0:
        alpha_list.append(v)

alpha_list.sort(reverse=True) #내림차순으로 정렬하고

result = 0
for j in range(len(alpha_list)): #9부터 배당
    result += alpha_list[j] * (9-j)

print(result)

#input이 크지 않다면 무리해서 for loop을 줄이기 보다는 여러번 돌리는 쪽으로 가는 것도 괜찮다
        


    
word = input().upper() #대문자 변환
word_list = list(set(word))

buffer = []
for alphabet in word_list:
    count = word.count(alphabet)
    buffer.append(count)
max = max(buffer)



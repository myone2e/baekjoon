words= list('abcdefghijklmnopqrstuvwxyz')
numbers = [n for n in range(1,27)]
dict = dict()
for i in range(len(words)):
    dict.update({ words[i]:numbers[i] })

print(dict)
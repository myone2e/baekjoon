eq = input().split('-') #minimum찾는 문제임에 따라 - 기준으로 split

if len(eq) == 1:
    sum = 0
    elements = eq[0].split('+')
    for num in elements:
        sum += int(num)

else:
    sum = 0
    elements = eq[0].split('+')
    for num in elements:
        sum += int(num)
        
    for sub in eq[1:]:
        sub = sub.split('+')
        for num in sub:
            sum -= int(num)

print(sum)

#eval은 0009 형식의 숫자 처리 불가능
#.split() 사용 시에는 ['44+55']에 사용 불가능 => str로 꺼내와서 사용 (line16)
eq = input().split('-') #minimum찾는 문제임에 따라 - 기준으로 split

def find_lost(eq):
    
    sum = eval(eq[0])
    if len(eq) == 1:
        return sum
    
    elif len(eq) > 1:
        for i in eq[1:]:
            temp = eval(i) #0009 이런 것 때문에 에러나는 경우 존재
            sum -= temp
    return sum
    
print(find_lost(eq))
            
        

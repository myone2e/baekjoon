import sys
def check_sum(nums):
    flag = False
    temp = []
    for s in reversed(nums):
        if flag == False:
            temp.append(s)
            flag = True
        else:
            double_s = str(int(s)*2)
            for c in double_s:
                temp.append(c)
            flag = False
    result = 0
    for n in temp:
        result += int(n)
    return result

for line in sys.stdin:
    nums = list(line.strip())
    print(check_sum(nums))
    
    
# 4294 =>  result = 4 + 1 + 8 + 2 + 4*2
# hello my name is min => Hello My Name is Min
import sys
input = sys.stdin.readline

nums = list(map(int, input().rstrip())) # 0은 어차피 버려도 됨.
nums = [n for n in nums if n!= 0]
nums.sort()

def plus_or_mult(nums):
    result = nums.pop(-1) # 최솟값으로 초기화하고
    for n in nums: # 나머지 숫자 다 더함
        result *= n  
    return result
print(plus_or_mult(nums))

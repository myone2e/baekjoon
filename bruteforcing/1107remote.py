# bruteforce => search for every single possible cases.
import sys
input = sys.stdin.readline
N = int(input()) # goal
M = int(input()) # number of broken buttons
broken = list(map(int, input().split()))

min_cnt = abs(100 - N)

for nums in range(1000001): # also have to check above the goal (500000 * 2)
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken: # find the value we can shift to!!
            break

        elif j == len(nums) - 1: # there aren't broken numbers => candidate for min count
            min_cnt = min(min_cnt, abs(int(nums) - N) + len(nums))

print(min_cnt)
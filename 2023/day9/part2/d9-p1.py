import re


def all_zeroes(nums):
    for x in nums:
        if x != 0:
            return False
    return True

def recurse(nums):
    if all_zeroes(nums):
        return [0] + nums
    ret = []
    for i,_ in enumerate(nums):
        if i != len(nums)-1:
            ret.append(nums[i+1]-nums[i])
    return [nums[0] - recurse(ret)[0]] + nums


f = open("input.txt", "r")

sum = 0

for line in f:
    temp = [int(x) for x in line.replace('\n', '').split(' ')]
    sum += recurse(temp)[0]
f.close()

print(f'The sum is {sum}')


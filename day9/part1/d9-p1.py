import re


def all_zeroes(nums):
    for x in nums:
        if x != 0:
            return False
    return True

def recurse(nums):
    if all_zeroes(nums):
        return nums + [0]
    ret = []
    for i,_ in enumerate(nums):
        if i != len(nums)-1:
            ret.append(nums[i+1]-nums[i])
    return nums + [nums[-1] + recurse(ret)[-1]]


f = open("input.txt", "r")

sum = 0

for line in f:
    temp = [int(x) for x in line.replace('\n', '').split(' ')]
    sum += recurse(temp)[-1]
f.close()

print(f'The sum is {sum}')


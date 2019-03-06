# -*- coding: utf-8 -*-

#My Answer
'''
def twoSum(nums, target):
    re_l = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                re_l.append(i)
                re_l.append(j)
                continue
    return(re_l)

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 26
    print(twoSum(nums, target))
'''

#One-Pass Hash Table
def twoSum(nums, target):
    dictionary = dict()
    pos = 0
    while pos < len(nums):
        if (target - nums[pos]) not in dictionary:
            dictionary[nums[pos]] = pos
            pos += 1
        else:
            return [dictionary[target - nums[pos]], pos]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 26
    print(twoSum(nums, target))








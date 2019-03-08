#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:39:37 2019

@author: mars
"""
"""
Determine whether an integer is a palindrome. An integer is 
a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right 
to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is 
not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

#My Answer
'''
def isPalindrome(x):
    num_str = str(x)
    res_list = []
    for i in range(len(num_str)):
        if num_str[i] == num_str[len(num_str) - 1 - i]:
            res_list.append(True)
        else:
            res_list.append(False)
    if False not in res_list:
        return True
    else:
        return False

if __name__ == "__main__":
    x = 12345654321
    print(isPalindrome(x))
'''

#Very Simple One
'''
def isPalindrome(x):
    return str(x) == str(x)[::-1]
'''

#Revert half of the number
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x / 10)
        return x == revertedNumber or x == int(revertedNumber / 10)

if __name__ == "__main__":
    x = 123454321
    print(isPalindrome(x))
























#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:04:18 2019

@author: mars
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose 
of this problem, assume that your function returns 0 when the reversed 
integer overflows.
"""

#My Answer
'''
def reverse(x):
    x_str_list = list(str(x))
    if x_str_list[0] == '-':
        x_rev_list = x_str_list[::-1]
        x_fin_str = '-'
        for i in range(len(x_rev_list)-1):
            x_fin_str += x_rev_list[i]
    elif x_str_list[0] == x_str_list[len(x_str_list)-1] == '0':
        x_fin_str = '0'
    elif x_str_list[len(x_str_list)-1] == '0':
        x_rev_list = x_str_list[::-1]
        x_fin_str = ''
        for i in range(1, len(x_rev_list)):
            x_fin_str += x_rev_list[i]
    else:
        x_rev_list = x_str_list[::-1]
        x_fin_str = ''
        for i in range(len(x_rev_list)):
            x_fin_str += x_rev_list[i]
    a = int(x_fin_str)
    if a >= -(2 ** 31) and a <= (2 ** 31) -1:
        return a
    else:
        return int('0')
    
if __name__ == "__main__":
    x = 123
    print(reverse(x))
'''

#Pop and Push Digits

def reverse(x):
    num_max = (2 ** 31) -1
    num_min = -(2 ** 31)
    rev = 0
    while x != 0:
        if x >= 0:
            pop = x % 10
        else:
            pop = x % (-10)
        if rev > num_max/10 or (rev == num_max/10 and pop > 7):
            return 0
        if rev < num_min/10 or (rev == num_min/10 and pop <-8):
            return 0
        rev = rev * 10 + pop
        x = int(x/10)
    return rev
    
if __name__ == "__main__":
    x = 123
    print(reverse(x))




















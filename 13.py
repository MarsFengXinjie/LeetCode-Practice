#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:04:01 2019

@author: mars
"""

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def romanToInt(s):
    value_dict = dict()
    value_dict['I'] = 1
    value_dict['V'] = 5
    value_dict['X'] = 10
    value_dict['L'] = 50
    value_dict['C'] = 100
    value_dict['D'] = 500
    value_dict['M'] = 1000
    value_dict['IV'] = 4
    value_dict['IX'] = 9
    value_dict['XL'] = 40
    value_dict['XC'] = 90
    value_dict['CD'] = 400
    value_dict['CM'] = 900
    
    s_list = []
    for alpha in s:
        s_list.append(alpha)
    
    s_list.append('I')
    final_list = []
    for i in range(len(s_list)-1):
        if value_dict[s_list[i]] >= value_dict[s_list[i+1]]:
            final_list.append(s_list[i])
        else:
            final_list.append(s_list[i] + s_list[i+1])
    
    final_list_1 = final_list
    for j in range(len(final_list)-1):
        try:
            if final_list[j][1] == final_list[j+1]:
                final_list_1.pop(j+1)
        except:
            continue
    
    final_int = 0
    for roman in final_list_1:
        final_int += value_dict[roman]
    
    return(final_int)


if __name__ == '__main__':
    s = 'MCMXCIV'
    print(romanToInt(s))


































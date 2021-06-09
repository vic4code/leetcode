#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 03:01:36 2021

@author: victor
"""

class Solution:
    def intToRoman(self, num: int) -> str:
  
        number_list = [1000,900,500,400,
                       100,90,50,40,
                       10,9,5,4,1]
        
        roman_dict = {1000:'M',
                      900:'CM',
                      500:'D',
                      400:'CD',
                      100:'C',
                      90:'XC',
                      50:'L',
                      40:'XL',
                      10:'X',
                      9:'IX',
                      5:'V',
                      4:'IV',
                      1:'I'
                      }
        
        string = ''
        while num > 0:
            
            for n in number_list:
                if num >= n:
                    Q = num // n
                    num = num % n
                    
                    string = string + roman_dict[n] * Q
        
        return string
            
        
if __name__ == '__main__':
    
    num = 1994
    
    ans = Solution().intToRoman(num)
    print(ans)
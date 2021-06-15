#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 01:02:58 2021

@author: victor
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        s_arr = s.split(' ')
        
        for string in s_arr:
            if string:
                s = string
                break
        
        length = len(s)
        num_selector = ''
    
        if s and s[0] == '-':
            
            valid_string = '-' + self.string_to_num(s[1:])
            
            if len(valid_string) > 1:
                int_output = int(valid_string)
                return self.int_overflow_check(int_output)
            else:
                return 0
            
        elif s and s[0] == '+':
            
            valid_string = '+' + self.string_to_num(s[1:])
            
            if len(valid_string) > 1:
                int_output = int(valid_string)
                return self.int_overflow_check(int_output)
            else:
                return 0
        
        elif s and s[0].isdigit():
            
            valid_string = self.string_to_num(s)
            
            if len(valid_string) >= 1:
                int_output = int(valid_string)
                return self.int_overflow_check(int_output)
            else:
                return 0
        
        else:
            return 0
            
    def string_to_num(self,s):
        
        valid_string = ''
        for i in range(len(s)):
            if s[i].isdigit():
                valid_string = valid_string + s[i]
            else:
                break

        return valid_string
    
    def int_overflow_check(self,num):
        
        if num < -2 ** 31:
            return -2 ** 31
        
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1

        else:
            return num
        
if __name__ == '__main__':
    
    s = "    42"
    s = "    -42"
    s = "4193 with words"
    s = "words and 987"
    s = "-91283472332"
    s = "3.14159"
    s = "   +0 123"
    
    ans = Solution().myAtoi(s)
    print(ans)
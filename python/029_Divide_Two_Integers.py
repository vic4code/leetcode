#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:50:14 2021

@author: victor
"""

class Solution(object):
    # def divide(self, dividend, divisor):
    #     """
    #     :type dividend: int
    #     :type divisor: int
    #     :rtype: int
    #     """
        
    #     quotient = 0        
    #     sign = -1 if dividend * divisor < 0 else 1
        
    #     dividend, divisor = abs(dividend), abs(divisor)
        
    #     while dividend >= divisor:
    #         dividend -= divisor
    #         quotient += 1
        
    #     return sign * quotient
        
    # Subtract 2 times divisor to boost calculation
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        res = 0        
        sign = -1 if dividend * divisor < 0 else 1
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
       
        return min(max(-2147483648, sign * res), 2147483647)
        
if __name__ == '__main__':
    
    dividend = 10
    divisor = 3
    
    dividend = 7
    divisor = -3
    
    dividend = 0
    divisor = 1
    
    dividend = 1
    divisor = 1

    ans = Solution().divide(dividend,divisor)
    
    print(ans)
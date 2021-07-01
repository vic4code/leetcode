#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:57:41 2021

@author: victor
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        numbers = [x for x in range(1, n + 1)]
        multiple_of_5 = numbers[4:n:5]
        
        res = 0
        print(multiple_of_5)
        for i in multiple_of_5:
            res += 1
            quotient = i // 5

            while quotient >= 5:
                if quotient % 5 == 0:   
                    res += 1
                    quotient = quotient // 5
                else:
                    break
   
        return res
        

if __name__ == '__main__':
    
    n = 30
    ans = Solution().trailingZeroes(n)
    
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:58:57 2021

@author: victor
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        elif n == 2:
            return 2
        
        else:
            first = 1
            second = 2
            
            for i in range(n - 2):
                res = first + second
                first = second
                second = res
            
            return res
            
        
        
if __name__ == '__main__':
    
    n = 5
    ans = Solution().climbStairs(n)
    
    print(ans)
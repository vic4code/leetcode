#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:47:54 2021

@author: victor
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        i = 1
        res = 0
        
        if x == 0:
            return res
        
        while i * i <= x:
            res = i
            i += 1
        
        return res
        
if __name__ == '__main__':
    
    x = 4
    x = 8
    
    ans = Solution().mySqrt(x)
    
    print(ans)
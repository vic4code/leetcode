#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:35:15 2021

@author: victor
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 1:
            return True
        
        if n % 3 != 0 or n <= 0:
            return False
        
        while n > 1:
            
            if n % 3 != 0:
                print(n)
                return False
            n = n // 3
            
        return True

if __name__ == '__main__':

    n = 27
    n = 45
    n = 9
    n = 0
    n = 1
    
    ans = Solution().isPowerOfThree(n)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:50:14 2021

@author: victor
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        n = str(n)
        summation = 0
        log = []
        
        while summation != 1:
            summation = 0
            
            for s in n:
                summation = summation + int(s) ** 2
            
            if summation not in log:
                log.append(summation)
            
            else:
                return False
            
            
            if summation == 1:
                return True
            
            else: 
                n = str(summation)
            
                
        return False
                     
        
if __name__ == '__main__':
    
  
    n = 19
    # n = 2
    # n = 1
    # n = 3
    
    ans = Solution().isHappy(n)
    
    print(ans)
    
    
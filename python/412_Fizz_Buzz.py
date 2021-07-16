#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:20:44 2021

@author: victor
"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        
        for i in range(1, n + 1):
            
            if i % 15 == 0:
                res.append("FizzBuzz")
                
            elif i % 3 == 0:
                res.append("Fizz")
                
            elif i % 5 == 0:
                res.append("Buzz")
            
            else:
                res.append(str(i))
                
        return res
            
        
        
if __name__ == '__main__':

    n = 15
    ans = Solution().fizzBuzz(n)
    print(ans)
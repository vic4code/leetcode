#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 01:57:11 2021

@author: victor
"""
class Solution(object):
#     def myPow(self, x, n):
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
        
#         return x ** n
    
    def myPow(self, x, n):
        if n < 0 :
            return 1 / self.helper(x, -n)
        else:
            return self.helper(x, n)
    
    def helper(self, x, n):
        if n == 0: 
            print(n)
            return 1
        print('n',n)
        half = self.helper(x, n // 2)
        
        print('lower part')
        print('half',half)
        if n % 2 == 0:
            print('n',n)
            return half * half
        else:
            print('n',n)
            return half * half * x
    
    
if __name__ == '__main__':
    
    x = 3
    n = 11
    ans = Solution().myPow(x,n)
    print(ans)
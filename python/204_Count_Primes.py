#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:19:51 2021

@author: victor
"""

class Solution(object):
    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
        
    #     if n == 0 or n == 1 :
    #         return 0
        
    #     else:
    #         count = 0
    #         for i in range(2,n):
                
    #             if self.isPrime(i):
    #                 # print(i)
    #                 count += 1
                    
    #         return count
            
    # def isPrime(self,k):
        
    #     i = 2
    #     res = True
    #     while i * i <= k:
    #         if k % i == 0:
    #             return False
    #             break
            
    #         i += 1
                
    #     return res
    def countPrimes(self, n):
        if n < 2:
            return 0
        
        s = [1] * n
        s[0] = s[1] = 0
        
        # Find Prime numbers which are the multiple number of i
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)
    
if __name__ == '__main__':
    
    n = 100
    ans = Solution().countPrimes(n)
    
    print(ans)
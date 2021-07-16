#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:09:36 2021

@author: victor
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = '1'
        
        for i in range(1,n):
            res = self.decompose(res)
        
        return res

    def decompose(self,s):
        
        length = len(s)
        number = s[0]
        count = 0
        res = ''
        
        for i in range(length):
            if number == s[i]:
                count += 1
                if i < length - 1:
                    if s[i] != s[i+1]:
                        res = res + str(count) + number
                        number = s[i+1]
                        count = 0

                elif i == length - 1:
                    res = res + str(count) + number
                    
        return res
    
if __name__ == '__main__':
    
    n = 6
    ans = Solution().countAndSay(n)
    print(ans)
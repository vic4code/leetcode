#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:59:47 2021

@author: victor
"""

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        s = s.replace('-','').upper()
        length = len(s)
        groups = length // k
        remainder = length % k
        res = ''
        
        if remainder == 0:
            
            for i in range(groups):
                res = res + s[k * i:k * (i + 1)] + '-'
            
            res = res[:-1]
            return res
        
        else:
            
            res = s[:remainder] + '-'
            
            for i in range(groups):
                res = res + s[(remainder + k * i):(remainder + k * (i + 1))] + '-'
            
            res = res[:-1]
            return res

if __name__ == '__main__':
    
    s = "5F3Z-2e-9-w"
    k = 4
    
    s = "2-5g-3-J"
    k = 2
    
    ans = Solution().licenseKeyFormatting(s,k)
    
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 01:15:14 2021

@author: victor
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False
                             
        
if __name__ == '__main__':
    
    s = "()[]{}"
    s = "{[]}"
    s = "()[]{}"
    s = "([)]"
    
    ans = Solution().isValid(s)
    print(ans)
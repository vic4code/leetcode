#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:03:55 2021

@author: victor
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        
        elif not haystack or not needle:
            return 0
        
        else: 
            for i in range(len(haystack)):
                if needle == haystack[i:i+len(needle)]:
                    return i
    
if __name__ == '__main__':
    
    
    haystack = "hello"
    needle = "ll"
    
    haystack = "aaaaa" 
    needle = "bba"
    
    haystack = ""
    needle = ""
    
    haystack = "mississippi"
    needle = "issip"
    
    ans = Solution().strStr(haystack,needle)
    print(ans)
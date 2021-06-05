#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 22:33:30 2021

@author: victor
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        longest = ""
        
        for i in range(len(s)):
            
            # Odd
            l, r = i, i
            while  l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l+1:r]
                    
                l -= 1
                r += 1

            # Even
            l, r = i, i + 1
            while  l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l+1:r]
                l -= 1
                r += 1
            
        return longest
    
if __name__ == '__main__':
    
    s = "babadbbb"
    s = "cbbd"
    s = "a"
    s = "ac"
    s = "caac"
    # s = "dvdf"
    # s = "anviaj"
    
    ans = Solution().longestPalindrome(s)
    print(ans)
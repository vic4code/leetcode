#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:34:04 2021

@author: victor
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(x for x in s if x.isalpha() or x.isnumeric()).lower()
        reverse_s = s[::-1]
        
        for i in range(len(s) // 2):
            if s[i] != reverse_s[i]:
                return False
        
        return True
        
if __name__ == '__main__':
    
    s = "A man, a plan, a canal: Panama"
    s = "abrbaasdf"
    ans = Solution().isPalindrome(s)
    
    print(ans)
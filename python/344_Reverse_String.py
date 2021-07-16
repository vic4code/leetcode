#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 03:25:21 2021

@author: victor
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        length = len(s)
        for i in range(length):
            s.append(s[-1-i])
            del(s[-2-i])

        return s
    
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
            
        return s
    
    def reverseString(self, s):
        s.reverse()
            
        return s
    
if __name__ == '__main__':
    
    s = ["h","e","l","l","o"]
    s = ["H","a","n","n","a","h"]
    ans = Solution().reverseString(s)
    
    print(ans)
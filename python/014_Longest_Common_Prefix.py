#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:58:24 2021

@author: victor
"""

class Solution:
    def longestCommonPrefix(self, strs):
        
        n_str = len(strs)
        first_str = strs[0]
        longest_prefix = ""
        
        for i in range(len(first_str)):
            common = 0
            prefix = first_str[:i+1]
            
            for str in strs:
                if prefix == str[:i+1]:
                    common += 1
                
            if common == n_str and len(prefix) > len(longest_prefix):
                longest_prefix = prefix
                    
        
        return longest_prefix
        
        
        
if __name__ == '__main__':
    
    # strs = ["dog","racecar","car"]
    strs = ["flower","flow","flight"]
    
    ans = Solution().longestCommonPrefix(strs)
    print(ans)
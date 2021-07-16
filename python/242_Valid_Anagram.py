#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:32:45 2021

@author: victor
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dict_s = self.build_dict(s)
        dict_t = self.build_dict(t)
        
        return dict_s == dict_t
        
        
    def build_dict(self,string):
        
        res = {}
        for s in string:
            if s not in res:
                res[s] = 1
            
            else:
                res[s] += 1
            
        return res

if __name__ == '__main__':
    

    s = "anagram"
    t = "nagaram"
    
    ans = Solution().isAnagram(s, t)
    print(ans)
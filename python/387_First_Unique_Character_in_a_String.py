#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:25:19 2021

@author: victor
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        keys = []
        values = []
        res = -1
        
        for x in s:
            if x not in keys:
                keys.append(x)
                values.append(1)
            
            else:
                values[keys.index(x)] += 1
        
        for key,val in zip(keys,values):
            if val == 1:
                res = s.index(key)
                return res
            
        return res

            
if __name__ == '__main__':

    s = "leetcode"
    s = "loveleetcode"
    # s = "aabb"
    
    ans = Solution().firstUniqChar(s)
    print(ans)
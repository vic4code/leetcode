#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:39:12 2021

@author: victor
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        paths = [0] * n
        paths[0] = 1
        
        for i in range(m):
            for j in range(1,n):
                paths[j] += paths[j-1]
                
        return paths[-1]

if __name__ == '__main__':
    
    m = 3
    n = 7
    
    ans = Solution().uniquePaths(m, n)
    print(ans)
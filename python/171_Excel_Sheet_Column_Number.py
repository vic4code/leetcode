#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 02:22:38 2021

@author: victor
"""
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        res = 0
        val = [i for i in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = dict(zip(letters, val))
        for s in columnTitle:
            res = res * 26 + d[s]
        return res
        
        
if __name__ == '__main__':
    
    columnTitle = "A"
    columnTitle = "ZY"
    ans = Solution().titleToNumber(columnTitle)
    
    print(ans)
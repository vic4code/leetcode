#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 02:51:41 2021

@author: victor
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        row = [1]
        
        for i in range(numRows - 1):
            row = self.calculate(row)
            
            res.append(row)
            
        return res
    
    def calculate(self,row):
        
        new_list = [1]
        i = 0
        while i < len(row) - 1:
            new_list.append(row[i] + row[i+1])
            i += 1
        
        new_list.append(1)

        return new_list
        
if __name__ == '__main__':
    
    numRows = 1
    ans = Solution().generate(numRows)
    
    print(ans)
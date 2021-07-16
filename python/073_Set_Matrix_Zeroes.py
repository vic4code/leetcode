#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:19:41 2021

@author: victor
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        zero_indices = []
        indices = [[]]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_indices.append([i,j])
        
        for zero_index in zero_indices:
            indices = indices + self.helper(zero_index,m,n)
            
        # print(set(indices))
        
        for index in indices:
            if index and matrix[index[0]][index[1]] != 0:
                matrix[index[0]][index[1]] = 0
            
        return matrix
    
    def helper(self,index,m,n):
        
        res = []
        
        for i in range(m):
            if i != index[0]:
                res.append([i,index[1]])
        
        for j in range(n):
            if j != index[1]:
                res.append([index[0],j])
                
        return res
        
if __name__ == '__main__':
    
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    ans = Solution().setZeroes(matrix)
    print(ans)
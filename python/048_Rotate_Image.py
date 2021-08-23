#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 01:04:03 2021

@author: victor
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # h is number of rows
        h = len(matrix)
        
        # rows to index
        n = h - 1
        
        # Determine the number of repeated cols (n // 2 + n % 2)
        for i in range(n // 2):
            for j in range(i,n - i):
                print(i,j)
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = tmp
                
                
        return matrix
    
if __name__ == '__main__':
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    ans = Solution().rotate(matrix)
    print(ans)
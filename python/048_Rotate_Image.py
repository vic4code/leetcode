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
        
        n = len(matrix[0])
        # Determine the number of repeated cols (n // 2 + n % 2)
        for i in range(n // 2 + n % 2):
            
            for j in range(n // 2):
                print(i,j)
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
                
        return matrix
    
if __name__ == '__main__':
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    ans = Solution().rotate(matrix)
    print(ans)
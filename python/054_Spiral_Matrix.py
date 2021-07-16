#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:37:23 2021

@author: victor
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m, n = len(matrix), len(matrix[0])
        length = m * n
        i, j = 0, 0
        res = []
        count = 0
        i_lower, j_lower = 0, 0
        i_upper, j_upper = m, n
        
        # print(length)
        while count < length: 
            
            # Right
            if i == i_lower:
                print('right')
                print('j_lower',j_lower,'j_upper',j_upper)
                for x in range(j_lower,j_upper):
                    if count < length:
                        res.append(matrix[i][j])
                        print(matrix[i][j])
                        count += 1
                        j += 1
                        
                j_upper -= 1
                i_lower += 1 
                j -= 1
                i += 1

            # Down
            if j == j_upper:
                print('down')
                for x in range(i_lower,i_upper):
                    if count < length:
                        res.append(matrix[i][j])
                        print(matrix[i][j])
                        count += 1
                        i += 1
                
                i_upper -= 1
                i -= 1
                j -= 1

            # Left
            if i == i_upper:
                print('left')
                print('j_upper',j_upper)
                for x in range(j_upper,j_lower,-1):
                    if count < length:
                        res.append(matrix[i][j])
                        print(matrix[i][j])
                        count += 1
                        j -= 1
                
                i -= 1
                j += 1

            # Up
            if j == j_lower:
                print('up')
                for x in range(i_upper,i_lower,-1):
                    if count < length:
                        res.append(matrix[i][j])
                        print(matrix[i][j])
                        count += 1
                        i -= 1
                
                j_lower += 1 
                i += 1
                j += 1
                    
        return res

        
if __name__ == '__main__':
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    
    ans = Solution().spiralOrder(matrix)
    print(ans)
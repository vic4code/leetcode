#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:50:00 2021

@author: victor
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                count += self.dfs(grid,i,j)
        
        return count
                    
                
    def dfs(self,grid,i,j):
        
        if (i >=0 and i < len(grid)) and (j >= 0 and j < len(grid[0])) and grid[i][j] == '1':
            grid[i][j] = '.'
            self.dfs(grid,i + 1,j)
            self.dfs(grid,i - 1,j)
            self.dfs(grid,i,j + 1)
            self.dfs(grid,i,j - 1)
            
            return 1 
        
        else:
            return 0
    
        
        
if __name__ == '__main__':
    
    grid = [
              ["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]
            ]
    
    grid = [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
            ]
                
    ans = Solution().numIslands(grid)
    print(ans)
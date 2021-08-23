#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 02:33:07 2021

@author: victor
"""
class Solution(object):
    # def solve(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: None Do not return anything, modify board in-place instead.
    #     """
        
    #     def helper(board,row,col):
            
    #         if (row,col) not in visited and (row >= 0 and row < m) and (col >= 0 and col < n):
    #             visited.append((row,col))
                
    #             if board[row][col] == 'O':
    #                 helper(board,row,col - 1)
    #                 helper(board,row,col + 1)
    #                 helper(board,row - 1,col)
    #                 helper(board,row + 1,col)
    #                 print((row,col))
                    
    #             if (row > 0 and row < m - 1) and (col > 0 and col < n - 1):
                    
    #                 if board[row][col - 1] == 'X' or \
    #                     board[row][col + 1] == 'X'or \
    #                     board[row - 1][col] == 'X'or \
    #                     board[row + 1][col] == 'X':
                    
    #                     board[row][col] = 'X'
                    
    #     m, n = len(board), len(board[0])
    #     visited = []
        
    #     for row in range(1, m - 1):
    #         for col in range(1, n - 1):
                
    #             if board[row][col] == 'O':
                    
    #                 helper(board,row,col)
                    
    #     return board
    
    # DFS
    def solve(self, board):
        if not board or not board[0]:
            return 
        
        m, n = len(board), len(board[0])
        
        # Mark the position if 'O' is at the bounds.
        # Check up and down first.
        for i in [0, m - 1]:
            for j in range(n):
                self.dfs(board, i, j)   
        
        # And then check left and right.
        for i in range(m):
            for j in [0, n - 1]:
                self.dfs(board, i, j)
        
        # If the position is '.', remain as 'O'.
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
        
        return board
                
    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '.'
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)
        

if __name__ == '__main__':
    
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    board = [["X","O","X"],["X","O","X"],["X","O","X"]]
    
    ans = Solution().solve(board)
    print(ans)
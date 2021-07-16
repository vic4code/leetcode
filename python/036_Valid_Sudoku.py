#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 01:48:01 2021

@author: victor
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Row and Columns Inspection
        for row in range(9):
            row_inspect = dict(zip([str(x) for x in range(1,10)],[0] * 9))
            col_inspect = dict(zip([str(x) for x in range(1,10)],[0] * 9))
            
            for col in range(9):
                if board[row][col] != ".":
                    row_inspect[board[row][col]] = row_inspect[board[row][col]] + 1
                    if row_inspect[board[row][col]] > 1:
                        return False
                
                if board[col][row] != ".":
                    col_inspect[board[col][row]] = col_inspect[board[col][row]] + 1
                    if col_inspect[board[col][row]] > 1:
                        return False
        
        # Blocks Inspection
        block = [[0,1,2],[3,4,5],[6,7,8]]
        
        for r in block:
            for c in block:
                inspect = dict(zip([str(x) for x in range(1,10)],[0] * 9))
                
                for i in range(3):
                    for j in range(3):
                        if board[r[i]][c[j]] != ".":
                            inspect[board[r[i]][c[j]]] = inspect[board[r[i]][c[j]]] + 1
                            if inspect[board[r[i]][c[j]]] > 1:
                                return False
                        
                        
        return True
    
if __name__ == '__main__':
    
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
            
    ans = Solution().isValidSudoku(board)
    print(ans)
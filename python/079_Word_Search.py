#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:55:45 2021

@author: victor
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        self.count = 0
        
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
                
        
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        self.count += 1
        print(self.count,i,j)
        if len(word) == 0: # all the characters are checked
            return True
        
        # Check if direction is valid or the current letter equals to the query letter.
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0]!= board[i][j]:
            return False
        
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        print('Gotcha',tmp)
        print(board)
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        print('count',self.count,tmp)
        board[i][j] = tmp
        print(board)
        return res
            
        
if __name__ == '__main__':
    

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"        
    ans = Solution().exist(board, word)
    print(ans)
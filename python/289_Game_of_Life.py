from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        states = [[0] * cols for _ in range(rows)] 

        for row in range(rows):
            for col in range(cols):
                states[row][col] = self.check_live(row, col, rows - 1, cols - 1, board)

        for row in range(rows):
            for col in range(cols):
                
                if states[row][col] == 1:
                    board[row][col] = 1
                    
                elif states[row][col] == -1:
                    board[row][col] = 0
        
        
    def check_live(self, i, j, i_max, j_max, board):
        
        current_stat = board[i][j]
        count = 0
        
        # Up
        if i - 1 >= 0:
            if board[i - 1][j] == 1:
                count += 1
        
        # Up Right
        if i - 1 >= 0 and j + 1 <= j_max:
            if board[i - 1][j + 1] == 1:
                count += 1
        
        # Right
        if j + 1 <= j_max:
            if board[i][j + 1] == 1:
                count += 1
        
        # Down Right
        if i + 1 <= i_max and j + 1 <= j_max:
            if board[i + 1][j + 1] == 1:
                count += 1
        
        # Down
        if i + 1 <= i_max:
            if board[i + 1][j] == 1:
                count += 1
        
        # Down Left
        if i + 1 <= i_max and j - 1 >= 0:
            if board[i + 1][j - 1] == 1:
                count += 1
        
        # Left
        if j - 1 >= 0:
            if board[i][j - 1] == 1:
                count += 1
        
        # Up Left 
        if i - 1 >= 0 and j - 1 >= 0:
            if board[i - 1][j - 1] == 1:
                count += 1

        # Final check
        if current_stat == 1:
            
            if count < 2:
                return -1
            
            if count == 2 or count == 3:
                return 1
                
            if count > 3:
                return -1

        else:
            if count == 3:
                return 1
            
        return 0
            

if __name__ == '__main__':

    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    ans = Solution().gameOfLife(board)

    print(board)
        
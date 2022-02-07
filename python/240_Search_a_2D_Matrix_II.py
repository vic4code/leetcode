from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        
        if row == 1:
            if target in matrix[0]:
                return True
        
        if col == 1:
            if target in [e[0] for e in matrix]:
                return True
        
        i, j = row - 1, 0
    
        while i > -1 and j < col:
   
            val = matrix[i][j]
            
            if val == target:
                return True
            
            if val < target:
                j += 1
                
            else:
                i -= 1

if __name__ == '__main__':

    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    ans = Solution().searchMatrix(matrix, target)

    print(ans)
                
                
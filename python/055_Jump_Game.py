#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:40:15 2021

@author: victor
"""
class Solution(object):
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
        
    #     n = len(nums)
        
    #     if n == 1:
    #         return True
        
    #     else:
    #         i = 0
    #         while i <= n - 1:
    #             max_val = nums[i]
                
    #             for x in range(1,max_val):
    #                 i = i + x
                    
    #                 if i == n - 1:
    #                     return True
                    
    #                 elif i < n - 1:
    #                     if nums[i] == 0:
    #                         return False
            
    #         return False
    
    def canJump(self, nums) -> bool:
        last_position = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1): # Iterate backwards from second to last item until the first item
            print(i, nums[i], last_position)
            if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
                last_position = i # Since we just need to reach to this new index
        return last_position == 0	
    
    
    ## DP solution
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [0] * length
        
        dp[0] = nums[0]
        
        for i in range(1, length - 1):
            
            # It means that you cannot go over the current index 
            print(dp[i-1],i)
            if dp[i - 1] < i:
                return False
            
            dp[i] = max(i + nums[i], dp[i - 1])
            
            if dp[i] >= length - 1:
                return True
        
        print(dp)
        return dp[length - 2] >= length - 1
        

if __name__ == '__main__':
    
    nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    # nums = [0]
    # nums = [1]
    # nums = [2,0]

    ans = Solution().canJump(nums)
    print(ans)
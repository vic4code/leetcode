#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:59:21 2021

@author: victor
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        currSum = maxSum = nums[0]
    
        for num in nums[1:]:
            # If the current num is larger than the sum of the previous numbers, there must be larger subarray behind. 
            currSum = max(num ,currSum + num)
            maxSum = max(maxSum, currSum)
            
        return maxSum
        
if __name__ == '__main__':
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-2,1]
    # nums = [-2,-1]
    
    ans = Solution().maxSubArray(nums)
    
    print(ans)
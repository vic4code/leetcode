#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:15:37 2021

@author: victor
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans
    
if __name__ == '__main__':

    nums = [0,1,0,0,3,12,1,2,3,4,6,0,0,5,5,5]
    ans = Solution().maxProduct(nums)
    print(ans)
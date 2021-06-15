#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:20:41 2021

@author: victor
"""

class Solution(object):
    # def threeSumClosest(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     res = 0
        
    #     for i in range(len(nums)-2):
    #         # If right is positive and equals to left, it has to be excluded.
    #         if nums[i] == nums[i-1]:
    #             continue
            
    #         l, r = i+1, len(nums)-1
            
    #         while l < r:
    #             s = nums[i] + nums[l] + nums[r]
    #             res = min(res, abs(s - target))

    #             # If the neighbor is the same, skip it to the next.
    #             while l < r and nums[l] == nums[l+1]:
    #                 l += 1
    #             while l < r and nums[r] == nums[r-1]:
    #                 r -= 1
    #             l += 1; r -= 1
        
    #     return res
    
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        res = float('inf')
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                    
                if s < target:
                    l += 1
                else:
                    r -= 1
             
            if abs(res - target) == 0:
                break
                
        return res
    
    
if __name__ == '__main__':
    
    nums = [-1,2,1,-4]
    target = 1
    
    ans = Solution().threeSumClosest(nums,target)
    
    print(ans)
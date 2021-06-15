#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:27:05 2021

@author: victor
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(nums)
        
        for i in range(length):
            
            if nums[i] >= target:
                return i
                
            elif i == length - 1:
                return length
            
        
if __name__ == '__main__':
    
    nums = [1,3,5,6]
    target = 7
    
    nums = [1]
    target = 0
    
    ans = Solution().searchInsert(nums,target)
    print(ans)
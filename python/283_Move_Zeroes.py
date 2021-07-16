#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 01:13:23 2021

@author: victor
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        for num in nums:

            if num == 0:
                nums.remove(num)
                nums.append(0)
                
        return nums
            
if __name__ == '__main__':

    nums = [0,1,0,0,3,12,1,2,3,4,6,0,0,5,5,5]
    ans = Solution().moveZeroes(nums)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 02:13:52 2021

@author: victor
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n < 3:
            return nums.index(max(nums))
        
        i, res = 1, 0

        while res == 0 and i + 1 < n:

            if nums[i - 1] < nums[i] and nums[i] > nums[i+1]:
                res = i
            
            i += 1
        
        if res != 0:
            return res
        
        else:
            return nums.index(max(nums))
        
if __name__ == '__main__':

    nums = [1,2,3,1]
    ans = Solution().findPeakElement(nums)
    print(ans)
        

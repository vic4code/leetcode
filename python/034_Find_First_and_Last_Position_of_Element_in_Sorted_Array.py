#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:57:14 2021

@author: victor
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) <= 1:
            if target not in nums:
                return [-1,-1]
            
            else: 
                return [0,0]

        center = len(nums) // 2
        band = []
        
        if target <= nums[center]:
            count = 0
            for n in nums[:center]:
                if target == n:
                    band.append(count)
                count += 1

        if target >= nums[center]:
            count = center
            for n in nums[center:]:
                if target == n and count not in band:
                    band.append(count)
                count += 1
        
        if not band:
            return [-1,-1]
        
        else:
            return [band[0],band[-1]]
        
        
if __name__ == '__main__':
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans = Solution().searchRange(nums, target)    
    print(ans)
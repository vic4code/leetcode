#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 03:19:32 2021

@author: victor
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n1 = 0
        n2 = 0 
        
        for i in range(len(nums)):
            for n in range(i+1,len(nums)):
                if nums[i] + nums[n] == target:
                    n1 = i
                    n2 = n
                    break
    
        return [n1,n2]
    
if __name__ == '__main__':
    
    nums = [2,7,11,15]
    target = 9
    ans = Solution().twoSum(nums, target)
    
    print(ans)
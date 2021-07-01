#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 02:20:38 2021

@author: victor
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        if len(nums) < 2:
            return nums[0]
        
        elif len(nums) % 2 == 1 and nums[-2] != nums[-1]:
            return nums[-1]
            
        else:
            i = 0
            while i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    i += 2
            
                else:
                    return nums[i]
                
        
        
if __name__ == '__main__':
    
    nums = [4,1,2,1,2]
    ans = Solution().singleNumber(nums)
    
    print(ans)
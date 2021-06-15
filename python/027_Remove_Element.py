#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:19:23 2021

@author: victor
"""

class Solution:
    def removeElement(self, nums, val):
    
        while val in nums:
            nums.remove(val)
            
        length = len(nums)
        
        return length
        
if __name__ == '__main__':
    
    nums = [3,2,2,3]
    val = 3
    
    ans = Solution().removeElement(nums,val)
    print(ans)
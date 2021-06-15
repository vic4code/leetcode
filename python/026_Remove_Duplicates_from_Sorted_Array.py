#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:40:25 2021

@author: victor
"""

class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums) <= 1:
            return len(nums), nums
        
        else:
            i = 0
            length = len(nums)
            
            while i < length - 1:
    
                if nums[i] == nums[i+1]:
                    del nums[i]
                    
                    length = len(nums)
                    i = 0
                
                else:
                    i += 1
    
            return len(nums), nums
        
        
if __name__ == '__main__':
    
    nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,1]
    
    ans, nums_ = Solution().removeDuplicates(nums)
    print(ans)
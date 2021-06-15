#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:37:01 2021

@author: victor
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # If right is positive and equals to left, it has to be excluded.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # If the neighbor is the same, skip it to the next.
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

if __name__ == '__main__':
    
    nums = [-1,0,1,2,-1,-4]

    ans = Solution().threeSum(nums)
    print(ans)
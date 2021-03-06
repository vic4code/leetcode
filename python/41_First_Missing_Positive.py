#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 01:54:53 2021

@author: victor
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        # nums.sort()
        # res = 1
        # for num in nums:
        #     if num == res:
        #         res += 1
        # return res
        for i in range(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
                
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
            
        return len(nums)+1


if __name__ == '__main__':

    nums = [1,2,0]
    ans = Solution().firstMissingPositive(nums)
    print(ans)
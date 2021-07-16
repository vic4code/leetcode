#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:42:04 2021

@author: victor
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nums = set(nums)
        
        for i in range(n+1):
            if i not in nums:
                return i
            
if __name__ == '__main__':

    nums = [1,2,3]
    ans = Solution().missingNumber(nums)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:00:33 2021

@author: victor
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums:
            nums = list(set(nums))
            nums.sort()
            n = len(nums)
            count = 1
            max_count = 1

            for i in range(n-1):
                if nums[i+1] - nums[i] == 1:
                    count += 1
                    max_count = max(max_count,count)

                else:
                    count = 1

            return max_count
        
        return 0
                
    
if __name__ == '__main__':
    
    nums = [0,3,7,2,5,8,4,6,0,1]
    ans = Solution().longestConsecutive(nums)
    print(ans)
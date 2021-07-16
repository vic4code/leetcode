#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:53:57 2021

@author: victor
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
        
        
if __name__ == '__main__':
    

    nums = [1,2,3]
    # nums = [4,1,0]
    # nums = [0]
    ans = Solution().subsets(nums)
    print(ans)
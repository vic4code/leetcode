#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 01:41:06 2021

@author: victor
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        keys = []
        values = []
        
        for i in nums:
            if i not in keys:
                keys.append(i)
                values.append(1)
            
            else:
                index = keys.index(i)
                values[index] += 1

        majority = keys[values.index(max(values))]
        
        return majority
        
if __name__ == '__main__':
    
    nums = [3,2,3]
    # nums = [2,2,1,1,1,2,2]
    
    ans = Solution().majorityElement(nums)
    
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:17:47 2021

@author: victor
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map = {}
        
        for i in nums:
            if str(i) not in hash_map:
                hash_map[str(i)] = 1
            
            else:
                hash_map[str(i)] += 1
            
            if hash_map[str(i)] > 1:
                return True
                break 
        
        return False

        
if __name__ == '__main__':
    
  
    nums = [1,2,3,1]
    nums = [1,1,1,3,3,4,3,2,4,2]
    ans = Solution().containsDuplicate(nums)
    
    print(ans)
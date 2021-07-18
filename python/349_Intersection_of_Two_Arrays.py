#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:53:31 2021

@author: victor
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        for num in nums1:
            if num in nums2:
                res.append(num)
                
        return res
    
if __name__ == '__main__':

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    
    ans = Solution().intersection(nums1, nums2)
    print(ans)
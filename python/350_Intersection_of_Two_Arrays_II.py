#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 02:40:43 2021

@author: victor
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1.sort()
        nums2.sort()
        res= []
        
        i = 0
        while i < len(nums1):
            if nums1[i] in nums2:
                dup = nums1[i]
                res.append(dup)
                nums1.remove(dup)
                nums2.remove(dup)
                i -= 1
                
            i += 1
                
        return res
        
        
if __name__ == '__main__':

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]
    
    nums1 = [1,2,2,1]
    nums2 = [2]
    
    ans = Solution().intersect(nums1, nums2)
    print(ans)
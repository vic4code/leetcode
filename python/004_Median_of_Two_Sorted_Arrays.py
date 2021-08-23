#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 02:28:04 2021

@author: victor
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Sort
        merged_list = []
        
        while nums1 or nums2:
            
            if nums1 and nums2 and nums1[0] < nums2[0]:
                merged_list.append(nums1.pop(0))
            
            elif nums1 and nums2 and nums2[0] < nums1[0]:
                merged_list.append(nums2.pop(0))
                
            else:
                if nums1:
                    merged_list.append(nums1.pop(0))
                
                if nums2:
                    merged_list.append(nums2.pop(0))
        
        # Derive median
        n = len(merged_list) - 1
        
        if n == 0:
            return merged_list[0]
        
        else:
            median = 0
            if n % 2 == 0:
                median = merged_list[(n + 1) // 2]

            else:
                i, j = n // 2, n // 2 + 1
                median = float(merged_list[i] + merged_list[j]) / float(2)

            return median

if __name__ == '__main__':

    nums1 = [1,2]
    nums2 = [3,4]
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print(ans)
        
        
            
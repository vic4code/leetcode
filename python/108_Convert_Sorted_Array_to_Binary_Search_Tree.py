#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:22:00 2021

@author: victor
"""

class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, lower, upper):
        if lower == upper:
            return None
        
        mid = (lower + upper) // 2
        # print('mid',mid,nums[mid])
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lower, mid)
        node.right = self.helper(nums, mid+1, upper)

        return node
    

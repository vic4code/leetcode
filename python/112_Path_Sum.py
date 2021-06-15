#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:00:29 2021

@author: victor
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        sum = sum - root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        # check left
        left = self.hasPathSum(root.left, sum)
        # check right
        right = self.hasPathSum(root.right, sum)
        return (left or right)


if __name__ == '__main__':
    
    root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
    targetSum = 22
    
    ans = Solution().hasPathSum(root,targetSum)
    print(ans)
    
    
    
    
    
    
    
    
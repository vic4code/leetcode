#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 02:12:49 2021

@author: victor
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        
        if root:
            depth = 1 
            depth = self.isNode(root,depth)
    
        return depth
                  
    def isNode(self,root,depth):
        
        if root:
            if root.left or root.right:
                depth += 1
                depth = max(self.isNode(root.left,depth),self.isNode(root.right,depth))

        return depth
            
            
            
        
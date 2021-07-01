#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 23:49:24 2021

@author: victor
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
     
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        self.helper(root,res)
        
        return res
        
    def helper(self,root,res):
        
        if root:
            if root.left:
                self.helper(root.left,res)
            
            res.append(root.val)
            
            if root.right:
                self.helper(root.right,res)
            
   
if __name__ == '__main__':
    
  
    root = [1,null,2,3]
    ans = Solution().inorderTraversal(root)
    
    print(ans)
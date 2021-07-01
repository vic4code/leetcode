#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:13:33 2021

@author: victor
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        root1 = root.left
        root2 = root.right
        res = self.helper(root1,root2)

        return res
            
    def helper(self, root1, root2):
        
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        return (root1.val == root2.val) and self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
            
        
if __name__ == '__main__':
    
  
    root = [1,null,2,3]
    ans = Solution().isSymmetric(root)
    
    print(ans)
        
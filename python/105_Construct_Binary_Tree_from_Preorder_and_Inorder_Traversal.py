#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 02:20:53 2021

@author: victor
"""
class TreeNode:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        print('pre',preorder)
        print('in',inorder)
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            print('Current node',root.val,'Inorder index:',ind)
            print('left---')
            root.left = self.buildTree(preorder, inorder[0:ind])
            print('right---')
            root.right = self.buildTree(preorder, inorder[ind+1:])
            
            return root
        
if __name__ == '__main__':
    
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    ans = Solution().buildTree(preorder, inorder)
    print(ans)
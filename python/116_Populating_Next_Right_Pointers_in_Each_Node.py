#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:52:13 2021

@author: victor
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
    
        cur = root
        next = root.left
        
        while cur.left:
            cur.left.next = cur.right
        
            if cur.next:
                cur.right.next = cur.left
                cur = cur.next
            else:
                cur = next
                next = cur.left            
    
        return root

if __name__ == '__main__':
    # Driver program to test above function
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    
    print("Level order traversal of binary tree is -")
    ans = Solution().connect(root)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:17:19 2021

@author: victor
"""

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
 
# Function to  print level order traversal of tree
def LevelOrder(root):
    ret = []
    level = [root]
    count = 0
    while root and level:
        currentNodes = []
        nextLevel = []
        print('i',count,'Node',[x.val for x in level])
        for node in level:
            # print(node.val)
            currentNodes.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        
        # print([x.val for x in nextLevel])
        ret.append(currentNodes)
        level = nextLevel
        count += 1

    return ret

if __name__ == '__main__':
    # Driver program to test above function
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(31)
    root.right.right = Node(32)
    root.left.left.left = Node(6)
    root.left.left.right = Node(7)
    
    print("Level order traversal of binary tree is -")
    ans = LevelOrder(root)
    print(ans)
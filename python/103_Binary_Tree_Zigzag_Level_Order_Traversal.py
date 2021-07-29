#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 02:48:28 2021

@author: victor
"""

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
 
# Function to  print level order traversal of tree
def zigzagLevelOrder(root):
    ret = []
    level = [root]
    flag = 1
    while root and level:
        currentNodes = []
        nextLevel = []
        print('Node',[x.val for x in level])
        for node in level:
            # print(node.val)
            currentNodes.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            
        ret.append(currentNodes[::flag])
        level = nextLevel
        flag *= -1

    return ret

if __name__ == '__main__':
    # Driver program to test above function
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    ans = zigzagLevelOrder(root)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:16:49 2021

@author: victor
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val) 

    def pop(self):
        """
        :rtype: None
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        
        
if __name__ == '__main__':
    
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
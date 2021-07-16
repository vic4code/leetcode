#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 01:43:52 2021

@author: victor
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        L = []
        current = head
        
        while current:
            L.append(current.val)
            current = current.next
        
        n = len(L)
        for i in range(n // 2):
            if L[i] != L[n - i - 1]:
                return False
        
        return True
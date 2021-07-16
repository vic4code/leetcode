#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:48:40 2021

@author: victor
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head and head.next:
        
            current = head
            res_head = ListNode(current.next.val)
            res_head.next = ListNode(current.val)
            res = res_head

            while current.next and current.next.next:
                current = current.next
                res_head = ListNode(current.next.val)
                res_head.next = res
                res = res_head

            return res_head
        
        else:
            return head
    
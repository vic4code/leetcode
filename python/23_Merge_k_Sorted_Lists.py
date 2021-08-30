#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:46:44 2021

@author: victor
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    
        List = []
        for list in lists:
            current = list

            while current:
                List.append(current.val)
                current = current.next

        List.sort()

        if List:
            res_head = ListNode(List[0])
            res_current = res_head

            for ele in List[1:]:
                res_current.next = ListNode(ele)
                res_current = res_current.next

            return res_head

        else:
            return ListNode().next
                
                
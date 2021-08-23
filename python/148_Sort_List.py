#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 12:28:25 2021

@author: victor
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
        
        L = []
        current = head
        
        while current:
            L.append(current.val)
            current = current.next
        
        L = sorted(L)
        
        res_head = ListNode(L[0])
        res_current = res_head
        
        for i in range(1,len(L)):
            res_current.next = ListNode(L[i]) 
            res_current = res_current.next
            
        return res_head
    
if __name__ == '__main__':
    
    head = ListNode(4)
    current = head
    current = current.next
    current = ListNode(2)
    current = current.next
    current = ListNode(1)
    current = current.next
    current = ListNode(3)
    
    ans = Solution().sortList(head)
    
    print(ans.val)
    
    
    
    
    
    
    
            
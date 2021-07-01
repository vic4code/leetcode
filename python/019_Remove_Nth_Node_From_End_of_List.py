#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:11:00 2021

@author: victor
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = ListNode()
        self.current = self.head
        
    def push(self, l):
        while self.current != None and self.current.next != None:
            self.current = self.current.next
        
        self.current.next = ListNode(l)
        
    def from_list(self, L):
        if len(L) > 0:
            for i in range(len(L)):
                # Give the first number
                if i == 0:
                    self.head.next = ListNode(L[i])
                # Push the remainder of the numbers
                else:
                    self.push(L[i])
                
    def display(self):
        self.current = self.head.next
        while self.current != None:
            print(self.current.val)
            self.current = self.current.next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        length = 0
        current = head
        
        # Calculate length
        while current:
            length += 1
            current = current.next
        
        if n == length:
            res = head.next
        
        else:
            # Back to head
            current = head.next
            res = ListNode(head.val)
            res_current = res
            
            for i in range(1,length):
                if i == length - n:
                    res_current.next = current.next
                    break
                
                else:
                    res_current.next = ListNode(current.val)
                    res_current = res_current.next
                    current = current.next

        return res
        
        
if __name__ == '__main__':
    
    l = [1,2,3,4,5]
    n = 5
    
    l = [1]
    n = 1
    
    l = [1,2]
    n = 1
    
    l = [1,2]
    n = 2
    
    L = LinkedList()
    L.from_list(l)
    # L.display()
    
    head = L.head.next
    ans = Solution().removeNthFromEnd(head, n)
    
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:31:37 2021

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
                    # print(L[i])
                # Push the remainder of the numbers
                else:
                    self.push(L[i])
     
    def display(self):
        self.current = self.head.next
        while self.current != None:
            print(self.current.val)
            self.current = self.current.next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        current = head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next

    
if __name__ == '__main__':
    
    print('L1:')
    L1 = LinkedList()
    L1.from_list([2,4,3])
    L1.display()
    
    print('L2:')
    L2 = LinkedList()
    L2.from_list([5,6,4])
    L2.display()
    
    l1 = L1.head
    l2 = L2.head
    
    sol = Solution().addTwoNumbers(l1,l2)
    ans = sol.next
    print('Answer:')
    while ans != None:
        print(ans.val)
        ans = ans.next
    
    
    
    
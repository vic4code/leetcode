#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:11:54 2021

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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        tailA = headA
        tailB = headB
        
        seen = set()
        
        while tailA:
            seen.add(tailA)
            tailA = tailA.next 
        
        while tailB:
            if tailB in seen:
                return tailB
            tailB = tailB.next
            
        return None
    
    
if __name__ == '__main__':
    
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5] 
    skipA = 2
    skipB = 3

    headA = ListNode()
    headB = ListNode()

    # Intersection Linked List 
    commonList = LinkedList()
    commonList.from_list([8,4,5])
    
    
    # Linked List A
    A = LinkedList()
    A.from_list([4,1])
    tailA = A.current.next
    tailA.next = commonList.head.next

        
    # Linked List B
    B = LinkedList()
    B.from_list([5,6,1])
    tailB = B.current.next
    tailB.next = commonList.head.next
    
    sol = Solution().getIntersectionNode(A.head,B.head)
    ans = sol.val
    print(ans)

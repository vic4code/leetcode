#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:35:28 2021

@author: victor
"""

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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        mergedList = ListNode()
        current = mergedList

        current1 = l1
        current2 = l2

        while current1 or current2:
            
            if current1 and current2:
                val1 = current1.val
                val2 = current2.val

                if val1 < val2:
                    current.next = ListNode(current1.val)
                    current = current.next
                    current1 = current1.next
                
                elif val1 == val2:
                    current.next = ListNode(current1.val)
                    current = current.next
                    current.next = ListNode(current1.val)
                    current = current.next
                    current1 = current1.next
                    current2 = current2.next
                
                elif val1 > val2:
                    current.next = ListNode(current2.val)
                    current = current.next
                    current2 = current2.next
                
            elif current1 and not current2:
                current.next = current1
                return mergedList.next
                
            elif current2 and not current1:
                current.next = current2
                return mergedList.next
                
              
        return mergedList.next
        
if __name__ == '__main__':
    
    l1 = [1,2,4]
    l2 = [1,3,4]
    
    L1 = LinkedList()
    L1.from_list(l1)
    
    L2 = LinkedList()
    L2.from_list(l2)
    
    
    ans = Solution().mergeTwoLists(L1.head.next,L2.head.next)
    print(ans)
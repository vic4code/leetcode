#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:36:41 2021

@author: victor
"""

class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(arr) > 1:
             # Finding the mid of the array
            mid = len(arr)//2
     
            # Dividing the array elements
            L = arr[:mid]
            
            # into 2 halves
            R = arr[mid:]
     
            # Sorting the first half
            self.sortColors(L)
     
            # Sorting the second half
            self.sortColors(R)
            
            arr = self.merge(arr,L,R)
            
        return arr              


    def merge(self,arr,L,R):
        i = j = k = 0
     
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
     
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
     
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr        
        
        
if __name__ == '__main__':
    
    nums = [2,0,2,1,1,0]
    nums = [2,0,2,1,1,0]
    ans = Solution().sortColors(nums)
    print(ans)
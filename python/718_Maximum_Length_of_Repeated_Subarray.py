#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:29:13 2021

@author: victor
"""
class Solution(object):
    # def findLength(self, A, B):
    #     memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    #     print(memo)
    #     for i in range(len(A) - 1, -1, -1):
    #         for j in range(len(B) - 1, -1, -1):
    #             if A[i] == B[j]:
    #                 print(i,j)
    #                 memo[i][j] = memo[i + 1][j + 1] + 1
                    
    #             print(memo)
    #     return max(max(row) for row in memo)
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        res = 0
        overlap_length = len(nums1) + len(nums2) - 1
        
        for i in range(overlap_length):
            print('nums1',-i-1,overlap_length-i,nums1[-i-1:overlap_length-i])
            print('nums2',i-overlap_length,i+1,nums2[i-overlap_length:i+1])
            op = self.conv(nums1[-i-1:overlap_length-i],nums2[i-overlap_length:i+1])
            res = max(res,op)
        
        return res
    
    def conv(self, s1, s2):
        
        res = 0
        count = 0
        
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                count += 1
                res = max(res,count)
            else:
                count = 0
            
        return res
                
    
if __name__ == '__main__':
    
    nums1 = [1,2,3,2,1,2]
    nums2 = [3,2,1,4,7]
    
    ans = Solution().findLength(nums1, nums2)
    print(ans)
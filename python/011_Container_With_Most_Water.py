#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 00:36:05 2021

@author: victor
"""

class Solution:
    def maxArea(self, height):

        maxArea = 0
        left = 0 
        right = len(height) - 1

        while right > left:
            
            valid_height = min(height[left],height[right])
            area = valid_height * (right - left)
            maxArea = max(maxArea,area)
            
            if height[left]  > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxArea    
        
if __name__ == '__main__':
    
    height = [1,8,6,2,5,4,8,3,7]
    height = [4,3,2,1,4]
    height = [1,2,1]
    
    ans = Solution().maxArea(height)
    print(ans)
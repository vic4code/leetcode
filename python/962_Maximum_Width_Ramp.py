#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:53:16 2021

@author: victor
"""

class Solution(object):
    # def maxWidthRamp(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
        
        # length = len(nums)
        # max_ramp = 0
        # ramp_exist = 0
        
        # i = 0
        
        # while i < length - 1:
            
        #     if nums[i] <= max(nums[i:]):
        #         j = i + 1
        #         while j < length:
        #             if nums[i] <= nums[j]:
        #                 ramp_exist = 1
        #                 ramp = j - i
                        
        #                 if ramp > max_ramp:
        #                     max_ramp = ramp

        #             j += 1
            
        #     else:
        #         i += 1
            
        #     i += 1
            
        # return max_ramp
            
        # if ramp_exist == 0:
        #     return 0
        
    
        # for i in range(length):
        #     for j in range(i,length):
        #         if nums[i] <= nums[j]:
        #             ramp_exist = 1
        #             ramp = j - i
    
        #             if ramp > max_ramp:
        #                 max_ramp = ramp
                    
        #             # Early stop
        #             if ramp == length:
        #                 break
                    
        # return max_ramp
            
        # if ramp_exist == 0:
        #     return 0
        
        
     # def maxWidthRamp(self, nums):   
     #    ans = 0
     #    m = float('inf')
     #    # Sort index based on value
     #    for i in sorted(range(len(nums)), key=nums.__getitem__):
     #        ans = max(ans, i - m)
     #        m = min(m, i)
     #    return ans
        
    def maxWidthRamp(self, nums):
       
        stack = []
        max_ramp = 0
        for i, a in enumerate(nums):
            # Find starts which follow a descending ordering
            if not stack or stack[-1][1] > a:
                print('start','i:',i,':a',a)
                stack.append((i, a))
                
            
            # Calculate ramp from the starts
            else:
                print('else','i:',i,':a',a)
                x = len(stack) - 1
                while x >= 0 and stack[x][1] <= a:
                    print(stack[x][0],i)
                    max_ramp = max(max_ramp, i - stack[x][0])
                    x -= 1
                
        print(stack)
        return max_ramp
    
if __name__ == '__main__':
    
    # nums = [6,0,8,2,1,5]
    nums = [9,8,9,1,0,1,9,40,0,4,1]
    
    ans = Solution().maxWidthRamp(nums)
    print(ans)
    
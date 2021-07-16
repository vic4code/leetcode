#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:18:22 2021

@author: victor
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        pivot = -1
        for n in range(len(nums) - 1):
            if nums[n + 1] < nums[n]:
                pivot = n
                break
        
        if pivot == -1:
            if target in nums:
                return nums.index(target)
            else:
                return -1
            
        else:
            if target >= nums[0]:
                count = 0
                for n in nums[:pivot+1]:
                    if target == n:
                        return count

                    count += 1

            elif target <= nums[-1]:
                count = pivot + 1
                for n in nums[pivot+1:]:
                    if target == n:
                        return count

                    count += 1
        
            return -1
        
if __name__ == '__main__':
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans = Solution().search(nums, target)    
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:18 2021

@author: victor
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        length = len(gas)
  
        for i in range(length):
            count = 0
            tank = 0
            j = i
            
            for times in range(length):
                
                if j > length - 1:
                    j = length - j
                tank = tank + gas[j] - cost[j]
                j += 1
                
                if tank < 0:
                    break
                
                else:
                    count += 1
        
            if count == length:
                return i
                
        return -1
        
        
if __name__ == '__main__':
    
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    
    gas = [2,3,4]
    cost = [3,4,3]
                
    ans = Solution().canCompleteCircuit(gas,cost)
    print(ans)
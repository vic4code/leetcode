#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:26:50 2021

@author: victor
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        res = 0
        length = len(prices)
        local_min = max(prices)
        
        for i in range(length - 1):
            if prices[i] < prices[i+1]:
                local_min = min(local_min,prices[i])
            
            res = max(res,prices[i+1] - local_min)

        return res
        
        
if __name__ == '__main__':
    
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,0,2,3,4,5,6,7,1,8,20]
    ans = Solution().maxProfit(prices)
    
    print(ans)
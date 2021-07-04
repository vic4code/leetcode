#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:09:25 2021

@author: victor
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        length = len(prices)
        maxprofit = 0
        
        for i in range(length - 1):
            if prices[i] < prices[i + 1]:
                maxprofit += prices[i + 1] - prices[i]
                
        return maxprofit
        
        
if __name__ == '__main__':
    
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,0,2,3,4,5,6,7,1,8,20]
    ans = Solution().maxProfit(prices)
    
    print(ans)
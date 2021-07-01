#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:29:33 2021

@author: victor
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        # print(dp)
        for i in range(n + 1):
            # print('i',i)
            for j in range(i):
                # print('j',j)
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                # print(dp[i])
        return dp[n]
        
if __name__ == '__main__':
    
    n = 3
    ans = Solution().generateParenthesis(n)
    
    print(ans)
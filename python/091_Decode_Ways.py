#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 01:45:13 2021

@author: victor
"""

# Approach: We generate a bottom up DP table.

# The tricky part is handling the corner cases (e.g. s = "30").

# Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].

# Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

# For example:
# s = "2111"
# index 0: extra base offset. dp[0] = 1
# index 1: # of ways to parse "2" => dp[1] = 1
# index 2: # of ways to parse "21" => "2 1" and "21", dp[2] = dp[1] + dp[0] = 2
# index 3: # of ways to parse "211" => "2 1 1", "21 1", "2 11" => dp[3] = dp[2] + dp[1] = 3
# index 4: # of ways to parse "2111" => ("2 1 1 1", "2 1 11"),("21 1 1", "21 11"), "2 11 1" => dp[4] = dp[3] + dp[2] = 5


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0:2] = [1,1]

        for i in range(2, len(s) + 1): 
            print('one step',s[i-1:i])
            print('two step',s[i-2:i])
            
            # One step jump
            if 0 < int(s[i-1:i]):    #(2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
            
            print(i,dp)
        
        print(dp)
        return dp[-1]
    
if __name__ == '__main__':

    s = "2111"
    ans = Solution().numDecodings(s)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:50:07 2021

@author: victor
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s) + 1) # dp[i] means s[:i] can be segmented into words in the wordDicts 
        dp[0] = True
        print('init dp',dp)
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(s[i: j+1])
                if dp[i] and s[i: j+1] in wordDict:
                    # print(s[i: j+1])
                    dp[j+1] = True
                    print(dp)
          
        print('final',dp)
        return dp[-1]


if __name__ == '__main__':

    s = "leetcode"
    wordDict = ["leet","code"]
    
    # s = "applepenapple"
    # wordDict = ["apple","pen"]
    
    # s = "catsandog"
    # wordDict = ["cats","dog","sand","and","cat"]
    
    # s = "cars"
    # wordDict = ["car","ca","rs"]
    
    ans = Solution().wordBreak(s,wordDict)
    print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:30:15 2021

@author: victor
"""
class Solution(object):
    def permute(self, nums):
        self.count = 0
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        self.count += 1
        # print(self.count)
        if not nums:
            res.append(path)
            # return # backtracking
        
        # print('nums',nums,'path',path,'res',res)
        
        for i in range(len(nums)):
            # print('nums',nums,'i',i,'nums[:i]',nums[:i],'nums[i+1:]',nums[i+1:],'path + nums[i]',nums[i])
            # print('new nums',nums[:i]+nums[i+1:],'new path',path+[nums[i]],'new res',res)
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
         
    
# dfs(nums = [1, 2, 3] , path = [] , result = [] )
# |____ dfs(nums = [2, 3] , path = [1] , result = [] )
# |      |___dfs(nums = [3] , path = [1, 2] , result = [] )
# |      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
# |           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
# |           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
#        |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
#             |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
    

if __name__ == '__main__':
    
    nums = [1,2,3,4]
    ans = Solution().permute(nums)
    print(ans)
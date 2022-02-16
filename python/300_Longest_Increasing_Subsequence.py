from typing import List 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        stacks = []
        start = nums[0]
        
        while nums:
            
            start = nums.pop(0)
            stack = [start]
            i = 0
            length = len(nums)
            
            while i < length:
                
                if nums[i] <= start:
                    start = nums.pop(i)
                    stack.append(start)
                    length = len(nums)
                    
                else:
                    i += 1
            
            stacks.append(stack)
       
        return len(stacks)
                
            
if __name__ == '__main__':

    nums = [4,10,4,3,8,9]
    ans = Solution().lengthOfLIS(nums)

    print(ans)
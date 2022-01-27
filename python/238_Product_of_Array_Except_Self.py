class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        p = 1
        
        for i in range(len(nums)):
            res[i] = res[i] * p
            p = nums[i] * p
            
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * p
            p = nums[i] * p
            
            
        return res


if __name__ == '__main__':
    
    nums = [1,2,3,4]
    ans = Solution().productExceptSelf(n)
    
    print(ans)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        for i in range(len(nums) - 1):
            
            if nums[i + 1] == nums[i]:
                return nums[i]
                
if __name__ == '__main__':

    n = [16, 16]
    ans = Solution().nums(n)

    print(ans)
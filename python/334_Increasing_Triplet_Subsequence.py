from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            
            elif num <= second:
                second = num
                
            else:
                return True
        
        return False

if __name__ == '__main__':

    nums = [1,2,3,4,5]
    ans = Solution().increasingTriplet(nums)
    print(ans)
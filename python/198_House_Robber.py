class Solution:
    def rob(self, A):
        if len(A) == 1: return A[0]
        dp = [*A]
        dp[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])
        return dp[-1]
    

if __name__ == '__main__':
    
    A = [1,2,3,1]
                
    ans = Solution().rob(A)
    print(ans)
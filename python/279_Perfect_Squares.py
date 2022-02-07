class Solution:
    def numSquares(self, n: int) -> int:
        
        i = 1
        square_list = []
        while i**2 <= n:
            square_list.append(i**2)
            i += 1

        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in square_list:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            
            toCheck = temp

        return cnt

if __name__ == '__main__':

    n = 16
    ans = Solution().numSquares(n)

    print(ans)
                
                
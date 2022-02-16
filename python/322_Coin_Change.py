from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # No need to use coins
        if amount == 0:
            return 0

        count = 0
        stack = [0]

        # The Max count should be 1 * amount + 1 (0 count)
        visited = [False] * (amount + 1)
        visited[0] = True

        while stack:

            temp = []
            count += 1

            for val in stack:
                for coin in coins:
                    new_val = val + coin

                    if new_val == amount:
                        return count

                    if new_val > amount:
                        continue

                    # Store only not visited values to save time
                    if not visited[new_val]:
                        visited[new_val] = True
                        temp.append(new_val)

            stack = temp

        return -1


if __name__ == '__main__':

    List = [156,265,40,280]
    amount = 9109

    ans = Solution().coinChange(List, amount)

    print(ans)
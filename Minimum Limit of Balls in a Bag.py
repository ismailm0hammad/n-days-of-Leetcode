# LeetCode 1760 : Minimum Limit of Balls in a Bag
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/
class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def numOperations(m):
            return sum((num - 1) // m for num in nums)

        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if numOperations(mid) <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return low
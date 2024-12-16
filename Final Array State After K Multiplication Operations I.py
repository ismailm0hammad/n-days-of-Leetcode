# LeetCode 3264 : Final Array State After K Multiplication Operations I
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minNum = min(nums)
            idx = nums.index(minNum)
            nums[idx] = nums[idx]*multiplier
        return nums
# LeetCode 494 : Target Sum
# https://leetcode.com/problems/target-sum/description/
class Solution:
  def findTargetSumWays(self, nums: list[int], target: int) -> int:
    total = sum(nums)
    if total < abs(target) or (total + target) % 2 == 1:
      return 0

    def knapsack(nums, target):
      dp = [0] * (target + 1)
      dp[0] = 1

      for num in nums:
        for i in range(target, num - 1, -1):
          dp[i] += dp[i - num]

      return dp[target]

    return knapsack(nums, (total + target) // 2)
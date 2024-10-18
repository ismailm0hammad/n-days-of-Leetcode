# LeetCode 2044 : Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
class Solution:
  def countMaxOrSubsets(self, nums: list[int]) -> int:
    ors = functools.reduce(operator.or_, nums)
    riz = 0

    def dfs(i: int, path: int) -> None:
      nonlocal riz
      if i == len(nums):
        if path == ors:
          riz += 1
        return

      dfs(i + 1, path)
      dfs(i + 1, path | nums[i])

    dfs(0, 0)
    return riz
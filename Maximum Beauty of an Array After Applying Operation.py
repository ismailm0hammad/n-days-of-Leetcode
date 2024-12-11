# LeetCode 2779 : Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/
class Solution:
  def maximumBeauty(self, nums: list[int], k: int) -> int:
    res = 0

    nums.sort()

    lt = 0
    for rt in range(len(nums)):
      while nums[rt] - nums[lt] > 2 * k:
        lt += 1
      res = max(res, rt - lt + 1)

    return res